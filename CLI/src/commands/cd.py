from src.command import ICommand

from os import chdir, path


class CommandCd(ICommand):
    def execute(self, pipe_input):
        if self._args:
            if len(self._args) > 1:
                return "cd: too many arguments"
            chdir(self._args[0])
            return ""

        chdir(path.expanduser("~"))
        return ""
