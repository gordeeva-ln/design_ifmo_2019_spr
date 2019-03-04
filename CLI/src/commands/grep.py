from src.command import ICommand

from argparse import ArgumentParser
import re


class GrepArguments:
    def __init__(self, args):
        parser = ArgumentParser()

        parser.add_argument('PATTERN')

        parser.add_argument('FILES', nargs='*')

        parser.add_argument(
            '-i', '--ignore-case',
            action='store_true',
            default=False
        )

        parser.add_argument(
            '-w', '--word-regexp',
            action='store_true',
            default=False
        )

        parser.add_argument(
            '-A', '--after-context',
            type=int,
            action='store',
            default=0
        )

        self.__parsed_args = parser.parse_args(args)

    def files(self):
        return self.__parsed_args.FILES

    def pattern(self):
        if self.__parsed_args.word_regexp:
            return r"\b{}\b".format(self.__parsed_args.PATTERN)

        return r"{}".format(self.__parsed_args.PATTERN)

    def ignore_case(self):
        return self.__parsed_args.ignore_case

    def after_context(self):
        return self.__parsed_args.after_context


class CommandGrep(ICommand):
    def __init__(self, args):
        super().__init__(args)
        self.__args = GrepArguments(args)

    def execute(self, pipe_input):
        if self.__args.files():
            pipe_input = ""
            for name in self.__args.files():
                try:
                    with open(name) as f:
                        pipe_input += f.read()
                        pipe_input += '\n'

                except IOError:
                    return "io error: %s" % name

        result = []
        re_pattern = self.__args.pattern()
        re_flags = re.IGNORECASE if self.__args.ignore_case() else 0
        after_context_counter = 0
        for line in pipe_input.splitlines(True):
            if after_context_counter > 0:
                result.append(line)
                after_context_counter -= 1
            else:
                match = re.findall(
                    re_pattern,
                    line,
                    flags=re_flags
                )

                if match:
                    result.append(line)
                    after_context_counter = self.__args.after_context()

        return ''.join(result[:-1])
