"""Development host TCP relay: loopback listeners into the isolated network."""
import json
import select
import socket
import socketserver
import subprocess
import threading


def serve(name, host_port, container_port):
    info = json.loads(subprocess.check_output(['docker', 'inspect', name]))[0]
    networks = info['NetworkSettings']['Networks']
    assert set(networks) == {'cbm-r026-isolated'}
    address = networks['cbm-r026-isolated']['IPAddress']

    class Relay(socketserver.BaseRequestHandler):
        def handle(self):
            try:
                with socket.create_connection((address, container_port), timeout=10) as upstream:
                    sockets = [self.request, upstream]
                    while True:
                        ready, _, _ = select.select(sockets, [], [], 120)
                        if not ready:
                            return
                        for stream in ready:
                            data = stream.recv(65536)
                            if not data:
                                return
                            (upstream if stream is self.request else self.request).sendall(data)
            except OSError:
                return

    class Server(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        daemon_threads = True

    Server(('127.0.0.1', host_port), Relay).serve_forever()


if __name__ == '__main__':
    threading.Thread(target=serve, args=('cbm-r026-fixture', 18089, 8999), daemon=True).start()
    serve('cbm-r026-webui', 18088, 8080)
