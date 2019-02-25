from src.command import ICommand


class CommandWc(ICommand):
    def execute(self, pipe_input):
        if self._args:
            lines, words, chars = 0, 0, 0
            for name in self._args:
                try:
                    with open(name) as f:
                        data = f.read()

                        lines += 1 + data.count('\n')
                        words += len(data.split())
                        chars += len(data)

                except IOError:
                    return "io error: %s" % name

            return "%d %d %d" % (lines, words, chars)

        if pipe_input:
            lines = 1 + pipe_input.count('\n')
            words = len(pipe_input.split())
            chars = len(pipe_input)
            return "%d %d %d" % (lines, words, chars)

        return "io error: missing input"
