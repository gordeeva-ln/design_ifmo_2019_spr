from src.command import ICommand


class CommandCat(ICommand):
    def execute(self, pipe_input):
        result = ""
        for name in self._args:
            try:
                with open(name) as f:
                    result += f.read()
            except IOError:
                result += "io error: %s\n" % name

        return result[:-1]
