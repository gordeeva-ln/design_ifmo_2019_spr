from src.command import ICommand

from os import listdir, path


class CommandLs(ICommand):
    def execute(self, pipe_input):
        if self._args:
            if len(self._args) > 1:
                return "ls: too many arguments"
            return "\n".join(listdir(self._args[0]))

        return "\n".join(listdir())
