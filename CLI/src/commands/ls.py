from src.command import ICommand

from os import listdir, path


'''
List information about the FILEs (the current directory by default). Sort entries alphabetically if none of -
'''


class CommandLs(ICommand):
    def execute(self, pipe_input):
        if self._args:
            if len(self._args) > 1:
                return "ls: too many arguments"
            if not path.isdir(self._args[0]):
                return "ls: cannot access {}: No such file or directory".format(self._args[0])
            return "\n".join(listdir(self._args[0]))

        return "\n".join(listdir())
