"""
Usage: deputy bash [options]

options:
    -x      Do something custom!

"""

from docopt import docopt
from subprocess import call

def run(argv):
    """bash bash bash!!!"""

    args = docopt(__doc__, argv)

    if args['-x']:
        call(['echo', 'bash bash bash!!!'])
