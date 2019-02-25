from unittest import TestCase

from src.preprocessor import get_preprocessor
from src.environment import get_environment


class TestIPreprocessor(TestCase):
    def test_1(self):
        env = get_environment()
        env.set("a", "123")

        pre = get_preprocessor()
        self.assertEqual(["123123"], pre.process("$a$a", env))

    def test_2(self):
        env = get_environment()

        pre = get_preprocessor()
        self.assertEqual(["$''"], pre.process('"$''"', env))

    def test_3(self):
        env = get_environment()
        env.set("a", "123")

        pre = get_preprocessor()
        self.assertEqual(["hello123"], pre.process("hello$a", env))
