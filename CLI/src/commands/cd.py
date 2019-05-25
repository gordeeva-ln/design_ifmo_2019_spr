from src.command import ICommand

from os import chdir, path


'''
Change Directory - change the current working directory to a specific Folder.
'''


class CommandCd(ICommand):
    def execute(self, pipe_input):
        if self._args:
            if len(self._args) > 1:
                return "cd: too many arguments"
            if not path.isdir(self._args[0]):
                return "cd: {}: No such file or directory".format(self._args[0])
            chdir(self._args[0])
            return ""

        chdir(path.expanduser("~"))
        return ""
