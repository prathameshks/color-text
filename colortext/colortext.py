import sys


def cprint(*values: object, sep: str = ' ', end: str | None = '\n',color: str = '',file=sys.stdout,flush: bool=False):
    values = [str(val) for val in values]
    data = str(color) + sep.join((values)) + "\033[0m" + end
    file.write(data)
    if flush:
        file.flush()
    return None

cprint("sample text",color="\033[38;5;44m",flush=True)

input()