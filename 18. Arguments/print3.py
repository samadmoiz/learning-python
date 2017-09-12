# from __future__ import print_function
"""
Emulate most of 3.x print function for use in 2.x (and 3.x).
Call signature: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""

import sys


def print3(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3('hello', 'sep', sep='-')
