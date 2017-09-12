"""
Use keyword only arguments
Call signature: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""

import sys


def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3('hello', 'sep', sep='-')
