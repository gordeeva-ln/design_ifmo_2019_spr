from src.commands.cat import CommandCat
from src.commands.echo import CommandEcho
from src.commands.exit import CommandExit
from src.commands.pwd import CommandPwd
from src.commands.wc import CommandWc
from src.commands.grep import CommandGrep


def get_commands():
    commands = {
        'cat':  CommandCat,
        'echo': CommandEcho,
        'wc':   CommandWc,
        'pwd':  CommandPwd,
        'exit': CommandExit,
        'grep': CommandGrep,
    }

    return commands
