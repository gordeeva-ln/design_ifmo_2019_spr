from src.commands.cat import CommandCat
from src.commands.echo import CommandEcho
from src.commands.exit import CommandExit
from src.commands.pwd import CommandPwd
from src.commands.wc import CommandWc
from src.commands.grep import CommandGrep
from src.commands.cd import CommandCd
from src.commands.ls import CommandLs


def get_commands():
    commands = {
        'cat':  CommandCat,
        'echo': CommandEcho,
        'wc':   CommandWc,
        'pwd':  CommandPwd,
        'exit': CommandExit,
        'grep': CommandGrep,
        'cd': CommandCd,
        'ls': CommandLs,
    }

    return commands
