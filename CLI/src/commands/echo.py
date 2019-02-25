from src.command import ICommand


class CommandEcho(ICommand):
    def execute(self, pipe_input):
        if self._args:
            return ' '.join(map(str, self._args))

        return pipe_input
