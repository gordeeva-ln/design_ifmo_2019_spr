from abc import ABCMeta, abstractmethod


class IEnvironment(metaclass=ABCMeta):
    @abstractmethod
    def set(self, name, value):
        """ set env variable """

    @abstractmethod
    def get(self, name):
        """ get env variable"""


class Environment(IEnvironment):
    def __init__(self):
        self.__storage = dict()

    def set(self, name, value):
        self.__storage[name] = value

    def get(self, name):
        if self.__storage.__contains__(name):
            return self.__storage[name]
        raise LookupError("not defined: %s" % name)


def get_environment():
    return Environment()
