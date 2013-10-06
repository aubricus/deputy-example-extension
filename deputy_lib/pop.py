"""
Usage: deputy pop [options]

options:
    -x      Do something custom!

"""

from docopt import docopt
from subprocess import call

def run(argv):
    """pop pop pop!!!"""

    args = docopt(__doc__, argv)

    if args['-x']:
        call(['echo', 'pop pop pop!!!'])
