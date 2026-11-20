"""The autopilot tick lock (scripts/autopilot.sh take_lock) after a power cut: a lock left behind whose pid now
belongs to another program, or that comes from a previous boot, must be taken over; a live tick's lock must hold."""
import os
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
with open(os.path.join(ROOT, 'scripts', 'autopilot.sh'), encoding='utf-8') as _f:
    SCRIPT = _f.read()


def functions(*names):
    out = []
    for n in names:
        # one-line function first, else up to the first closing brace at column 0
        m = (re.search(rf'^{n}\(\) \{{[^\n]*\}}$', SCRIPT, re.M)
             or re.search(rf'^{n}\(\) \{{\n.*?^\}}$', SCRIPT, re.S | re.M))
        assert m, n
        out.append(m.group(0))
    return '\n'.join(out)


@unittest.skipUnless(shutil.which('bash') and shutil.which('ps'), 'needs bash and ps')
class TickLockTest(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.lock = os.path.join(self.d, 'lock')
        self.procs = []

    def tearDown(self):
        for p in self.procs:
            p.kill()
            p.wait()
        shutil.rmtree(self.d, ignore_errors=True)

    def spawn(self, argv0):
        p = subprocess.Popen(['bash', '-c', f'exec -a {argv0} sleep 60'])
        self.procs.append(p)
        return p.pid

    def write_lock(self, pid, boot=None):
        os.mkdir(self.lock)
        with open(os.path.join(self.lock, 'pid'), 'w') as f:
            f.write(f'{pid}\n')
        if boot is not None:
            with open(os.path.join(self.lock, 'boot'), 'w') as f:
                f.write(f'{boot}\n')

    def tick(self):
        body = (f'LOCK={self.lock!r}; log() {{ echo "$*"; }}\n' + functions('boot_id', 'lock_held', 'take_lock')
                + '\ntake_lock; echo TOOK; cat "$LOCK/pid"; trap - EXIT\n')
        return subprocess.run(['bash', '-c', body], capture_output=True, text=True, timeout=30)

    def current_boot(self):
        return subprocess.run(['bash', '-c', functions('boot_id') + '\nboot_id'], capture_output=True, text=True).stdout.strip()

    def test_free_lock_taken(self):
        r = self.tick()
        self.assertIn('TOOK', r.stdout)

    def test_pid_reused_by_other_program_is_taken_over(self):
        self.write_lock(self.spawn('com.apple.audio.helper'), self.current_boot())
        r = self.tick()
        self.assertIn('stale lock removed', r.stdout)
        self.assertIn('TOOK', r.stdout)

    def test_lock_from_previous_boot_is_taken_over(self):
        if not self.current_boot():
            self.skipTest('no kern.boottime on this system')
        self.write_lock(self.spawn('autopilot.sh'), '1')
        r = self.tick()
        self.assertIn('TOOK', r.stdout)

    def test_live_tick_of_this_boot_keeps_the_lock(self):
        self.write_lock(self.spawn('autopilot.sh'), self.current_boot())
        r = self.tick()
        self.assertEqual(r.returncode, 0)
        self.assertNotIn('TOOK', r.stdout)

    def test_old_format_lock_without_boot_file(self):
        self.write_lock(self.spawn('autopilot.sh'))
        self.assertNotIn('TOOK', self.tick().stdout)
        shutil.rmtree(self.lock)
        self.write_lock(self.spawn('some-other-program'))
        self.assertIn('TOOK', self.tick().stdout)


if __name__ == '__main__':
    unittest.main()
