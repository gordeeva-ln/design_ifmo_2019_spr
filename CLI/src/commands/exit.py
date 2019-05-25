from src.command import ICommand


class CommandExit(ICommand):
    def execute(self, pipe_input):
        quit(0)
