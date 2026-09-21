"""Supervise a quiet_window holder and bounded local subprocesses.

Not installed. Killing an SSH transport does not prove a remote effect stopped:
the durable checkpoint journal must retain its uncertain intent for reconciliation.
Acknowledgment is allowed only after the caller verifies actual remote evidence.
"""
import json
import os
import select
import signal
import subprocess
import threading
import time


class LeaseLost(RuntimeError):
    pass


class LeaseSupervisor:
    def __init__(self, command, job_id, nonce, *, interval=5, reply_timeout=5):
        if interval <= 0 or reply_timeout <= 0:
            raise ValueError("positive heartbeat bounds required")
        self.job_id, self.nonce = job_id, nonce
        self.interval, self.reply_timeout = interval, reply_timeout
        self.failed = threading.Event()
        self.stopping = threading.Event()
        self.mutex = threading.Lock()
        self.sequence = 0
        self.buffer = b""
        self.inodes = None
        self.process = subprocess.Popen(command, stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.DEVNULL, bufsize=0,
                                        start_new_session=True)
        self.thread = None
        try:
            self._response("ready", 0)
            self.thread = threading.Thread(target=self._heartbeat, daemon=True)
            self.thread.start()
        except BaseException:
            self.failed.set()
            self._terminate(self.process)
            self._close_pipes()
            raise

    def _response(self, kind, sequence):
        deadline = time.monotonic() + self.reply_timeout
        while b"\n" not in self.buffer:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise LeaseLost("lock holder unavailable")
            readable, _, _ = select.select([self.process.stdout], [], [], remaining)
            if not readable:
                raise LeaseLost("lock holder response timed out")
            chunk = os.read(self.process.stdout.fileno(), 4096)
            if not chunk:
                raise LeaseLost("lock holder disconnected")
            self.buffer += chunk
            if len(self.buffer) > 16384:
                raise LeaseLost("oversized lock holder response")
        line, self.buffer = self.buffer.split(b"\n", 1)
        try:
            response = json.loads(line)
        except (ValueError, UnicodeError) as exc:
            raise LeaseLost("invalid lock holder response") from exc
        expected = {"kind": kind, "sequence": sequence,
                    "job_id": self.job_id, "nonce": self.nonce}
        if not isinstance(response, dict) or any(response.get(k) != v for k, v in expected.items()):
            raise LeaseLost("lock holder identity or sequence mismatch")
        inodes = response.get("lock_inodes")
        from quiet_window import LOCKS
        if not isinstance(inodes, dict) or set(inodes) != set(LOCKS) or any(
            not isinstance(pair, list) or len(pair) != 2 or
            any(type(value) is not int or value < 0 for value in pair)
            for pair in inodes.values()
        ):
            raise LeaseLost("invalid lock holder inode evidence")
        if self.inodes is not None and inodes != self.inodes:
            raise LeaseLost("lock holder inode evidence changed")
        self.inodes = inodes
        return response

    def _exchange(self, operation, kind, **fields):
        with self.mutex:
            if self.failed.is_set() or self.process.poll() is not None:
                raise LeaseLost("lock holder unavailable")
            self.sequence += 1
            message = dict(operation=operation, job_id=self.job_id,
                           nonce=self.nonce, sequence=self.sequence, **fields)
            try:
                self.process.stdin.write((json.dumps(message) + "\n").encode())
                self.process.stdin.flush()
                return self._response(kind, self.sequence)
            except Exception as exc:
                self.failed.set()
                raise LeaseLost("lock holder exchange failed") from exc

    def _heartbeat(self):
        while not self.stopping.wait(self.interval):
            try:
                self._exchange("ping", "alive")
            except Exception:
                self.failed.set()
                return

    def check(self):
        """Require a fresh response, not merely a cached live-process flag."""
        if self.stopping.is_set():
            raise LeaseLost("lock holder supervisor closed")
        self._exchange("ping", "alive")

    def acknowledge(self, manifest_hash):
        """Call only after real off-host and PBS verification under this lease."""
        self.check()
        result = self._exchange("ack", "acknowledged", manifest_sha256=manifest_hash)
        if result.get("manifest_sha256") != manifest_hash:
            self.failed.set()
            raise LeaseLost("checkpoint acknowledgment identity mismatch")

    def run(self, command, *, timeout, stdout=None, stdin=None):
        """Run one bounded effect; private output belongs in caller-owned files.

        stdout defaults to DEVNULL. Never return raw stderr/provider data. Any
        exception after start requires reconciliation of that journaled effect.
        """
        if timeout <= 0:
            raise ValueError("positive effect deadline required")
        self.check()
        child = subprocess.Popen(command, stdin=stdin if stdin is not None else subprocess.DEVNULL,
                                 stdout=stdout if stdout is not None else subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL, start_new_session=True)
        deadline = time.monotonic() + timeout
        try:
            while child.poll() is None:
                if self.failed.is_set() or self.process.poll() is not None:
                    raise LeaseLost("lock holder lost during effect; reconcile intent")
                if time.monotonic() >= deadline:
                    raise TimeoutError("effect deadline exceeded; reconcile intent")
                self.failed.wait(min(.05, max(0, deadline - time.monotonic())))
            self.check()
            if child.returncode:
                raise RuntimeError("effect failed; reconcile intent")
        finally:
            self._terminate(child)

    @staticmethod
    def _terminate(process):
        # Only target our still-owned process group. Adapters must await all
        # children; exited SSH transports require remote-state reconciliation.
        if process.poll() is not None:
            return
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        except PermissionError:
            if process.poll() is None:
                raise
        try:
            process.wait(timeout=.5)
        except subprocess.TimeoutExpired:
            pass
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        except PermissionError:
            if process.poll() is None:
                raise
        process.wait(timeout=2)

    def _close_pipes(self):
        for stream in (self.process.stdin, self.process.stdout):
            if stream is not None:
                stream.close()

    def close(self):
        if self.stopping.is_set():
            return
        self.stopping.set()
        if self.thread is not None:
            self.thread.join(timeout=self.reply_timeout + 1)
        try:
            if not self.failed.is_set():
                self._exchange("release", "released")
                self.process.wait(timeout=self.reply_timeout)
        except Exception:
            self.failed.set()
        finally:
            self._terminate(self.process)
            self._close_pipes()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
