from unittest import TestCase

from src.environment import get_environment


class TestIEnvironment(TestCase):
    def test_1(self):
        env = get_environment()
        env.set("VAR", "123")
        self.assertEqual(env.get("VAR"), "123")

    def test_2(self):
        env = get_environment()
        self.assertRaises(LookupError, env.get, "VAR")
