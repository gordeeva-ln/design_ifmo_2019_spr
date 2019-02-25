from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):
    def __init__(self, args):
        self._args = args

    @abstractmethod
    def execute(self, pipe_input):
        """ execute command """
