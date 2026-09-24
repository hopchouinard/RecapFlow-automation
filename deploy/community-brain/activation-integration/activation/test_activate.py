import copy
import json
from pathlib import Path
import tempfile
import unittest
from activate import Activation, Docker, fingerprint
from unittest.mock import patch
from types import SimpleNamespace


def row(name):
    return {'Id': name, 'Image': 'sha256:fixture', 'Config': {'User': '', 'Cmd': ['serve']},
            'HostConfig': {'Memory': 1, 'NanoCpus': 1, 'ReadonlyRootfs': True, 'PortBindings': {}},
            'Mounts': [], 'State': {'Running': True},
            'NetworkSettings': {'Networks': {'isolated': {'IPAddress': '127.0.0.1'}}}}


class Engine:
    def __init__(self): self.rows = {'old': row('old')}; self.events = []; self.lost = False
    def inspect(self, name): return copy.deepcopy(self.rows.get(name))
    def stop(self, name): self.events.append(('stop', name)); self.rows[name]['State']['Running'] = False
    def start(self, name): self.events.append(('start', name)); self.rows[name]['State']['Running'] = True
    def create(self, plan, target):
        name = target['container']; self.events.append(('create', name)); self.rows[name] = row(name)
        if self.lost: self.lost = False; raise RuntimeError('lost acknowledgment')
    def health(self, row, target): pass


class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name); hold = root/'paused'; hold.write_text('preserve')
        self.engine = Engine(); self.journal = root/'journal.json'
        self.plan = {'holds': [str(hold)], 'incumbent': {'container': 'old', 'id': 'old',
                     'fingerprint': fingerprint(self.engine.rows['old'])},
                     'candidates': [{'container': 'new', 'image': 'sha256:fixture', 'network': 'isolated',
                     'runtime': {'memory': 1, 'nano_cpus': 1, 'read_only_root': True, 'user': '',
                                 'command': ['serve'], 'ports': {}, 'binds': [], 'volumes': []}}]}
    def controller(self): return Activation(self.plan, 'fixture-plan', self.journal, self.engine)

    def test_absent_container_is_distinct_from_daemon_failure(self):
        for message in (b'error: no such object: fixture', b'Error: No such container: fixture'):
            with patch('activate.subprocess.run', return_value=SimpleNamespace(returncode=1, stderr=message)), patch('activate.command', return_value=b'engine'):
                self.assertIsNone(Docker().inspect('fixture'))
        with patch('activate.subprocess.run', return_value=SimpleNamespace(returncode=1, stderr=b'daemon unavailable')), patch('activate.command', side_effect=RuntimeError('offline')):
            with self.assertRaises(RuntimeError): Docker().inspect('fixture')

    def test_volume_name_collision_is_not_a_container(self):
        with patch('activate.subprocess.run', return_value=SimpleNamespace(returncode=1, stderr=b'no such container')) as run, patch('activate.command', return_value=b'engine'):
            self.assertIsNone(Docker().inspect('volume-only'))
            self.assertEqual(run.call_args.args[0], ['docker', 'inspect', '--type', 'container', 'volume-only'])

    def test_docker_mount_order_does_not_invent_drift(self):
        first = row('old')
        first['Mounts'] = [{'Destination': '/state/z'}, {'Destination': '/state/a'}]
        second = copy.deepcopy(first); second['Mounts'].reverse()
        self.assertEqual(fingerprint(first), fingerprint(second))

    def test_activation_and_duplicate_do_not_repeat_effects(self):
        self.controller().activate(); events = list(self.engine.events)
        self.controller().activate(); self.assertEqual(events, self.engine.events)

    def test_lost_create_ack_reconciles_existing_container(self):
        self.engine.lost = True
        with self.assertRaises(RuntimeError): self.controller().activate()
        self.controller().activate()
        self.assertEqual(self.engine.events.count(('create', 'new')), 1)

    def test_absent_uncertain_candidate_is_not_recreated(self):
        self.engine.lost = True
        with self.assertRaises(RuntimeError): self.controller().activate()
        del self.engine.rows['new']
        with self.assertRaises(RuntimeError): self.controller().activate()
        self.assertEqual(self.engine.events.count(('create', 'new')), 1)

    def test_rollback_retains_candidate_and_restarts_original_id(self):
        self.controller().activate(); self.controller().rollback()
        self.assertFalse(self.engine.rows['new']['State']['Running'])
        self.assertTrue(self.engine.rows['old']['State']['Running'])
        self.assertEqual(self.controller().state['phase'], 'rolled_back')
        with self.assertRaises(ValueError): self.controller().activate()

    def test_hold_drift_refuses_further_actions(self):
        self.controller().activate(); before = list(self.engine.events)
        Path(self.plan['holds'][0]).write_text('changed')
        with self.assertRaises(ValueError): self.controller().rollback()
        self.assertEqual(before, self.engine.events)

    def test_unknown_candidate_is_not_adopted(self):
        self.engine.rows['new'] = row('new')
        with self.assertRaises(ValueError): self.controller().activate()
        self.assertEqual(self.engine.events, [])

    def test_changed_incumbent_is_not_restarted(self):
        self.controller().activate(); before = list(self.engine.events)
        self.engine.rows['old']['Config']['Cmd'] = ['different']
        with self.assertRaises(ValueError): self.controller().rollback()
        self.assertEqual(before, self.engine.events)

    def test_foreign_plan_cannot_resume_journal(self):
        self.controller().activate()
        with self.assertRaises(ValueError): Activation(self.plan, 'other', self.journal, self.engine)


if __name__ == '__main__': unittest.main()
