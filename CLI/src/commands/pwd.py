from src.command import ICommand

from os import getcwd


class CommandPwd(ICommand):
    def execute(self, pipe_input):
        return getcwd()
