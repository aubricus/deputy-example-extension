"""Usage:
    ext command
    ext command [-o | --opt]
    ext command <arg>
    ext [-h | --help]

    Lorem ipsum dolor.

    Examples:
        $ ext command
        $ ext command -o | --opt

    Arguments
        <arg>           Example arguments.

    Options:
        -o --opt        Example option.
        -h --help       Displays this message.
"""

import sys
from docopt import docopt


def main():
    arguments = docopt(__doc__)

    print(arguments)


if __name__ == "__main__":
    sys.exit(main())
