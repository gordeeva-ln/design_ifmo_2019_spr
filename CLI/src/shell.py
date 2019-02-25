from src.environment import get_environment
from src.preprocessor import get_preprocessor
from src.command_factory import get_commands

import subprocess
import sys


class Shell:
    def __init__(self):
        self.__env = get_environment()
        self.__cmd = get_commands()
        self.__pre = get_preprocessor()

    def __execute(self, tokens, buffer):
        if not tokens:
            return buffer

        # group token by pipes
        try:
            pipe_index = tokens.index('|')
        except ValueError:
            pipe_index = len(tokens)

        command = tokens[:pipe_index]

        if not Shell.__is_assignment(command):
            if command[0] in self.__cmd:  # built-in command
                cmd = self.__cmd[command[0]](command[1:])
                buffer = cmd.execute(buffer)
            else:  # unknown command
                try:
                    buffer = subprocess.check_output(command, stderr=sys.stderr).decode("utf-8")
                except subprocess.CalledProcessError:
                    # abort execution
                    return "non-zero exit status:  %s" % command
        else:
            # ignore assignment + reset buffer
            buffer = ""

        return self.__execute(tokens[pipe_index + 1:], buffer)

    @staticmethod
    def __is_assignment(tokens):
        return len(tokens) == 1 and '=' in tokens[0]

    def __assign(self, tokens):
        [name, value] = tokens[0].split('=')
        self.__env.set(name, value)

    def run(self):
        while True:
            line = input('> ')
            tokens = self.__pre.process(line, self.__env)
            if Shell.__is_assignment(tokens):
                self.__assign(tokens)
            else:
                result = self.__execute(tokens, "")
                print(result)
