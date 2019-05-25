from unittest import TestCase

from src.command_factory import get_commands


class TestICommand(TestCase):
    def test_cd(self):
        comm = get_commands()

        cd = comm['cd']([])
        pwd = comm['pwd']([])
        path = (pwd.execute()).split('\\')
        cd.execute()
        self.assertEqual(pwd.execute(), "\\".join(path[:-1]))

    def test_ls(self):
        comm = get_commands()

        ls = comm['ls']([])
        self.assertEqual(ls.execute(), '\n'.join(['cli.py', 'src', 'tests']))
