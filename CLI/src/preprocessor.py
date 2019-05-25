from abc import ABCMeta, abstractmethod

import shlex


class IPreprocessor(metaclass=ABCMeta):
    @abstractmethod
    def process(self, line, env):
        """ preprocess line """


class Preprocessor(IPreprocessor):
    def process(self, line, env):
        def transform(token):
            parts = token.split('$')

            acc = [parts[0]]
            for part in parts[1:]:
                if part and part[0] not in ['"', "'"]:
                    name = shlex.split(part)[0]
                    try:
                        value = env.get(name)
                    except LookupError:
                        value = ""  # ~bash

                    acc[len(acc) - 1] += part.replace(name, value, 1)
                else:
                    acc.append(str(part))

            return '$'.join(acc)

        return list(map(transform, shlex.split(line)))


def get_preprocessor():
    return Preprocessor()
