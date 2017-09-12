#!/usr/bin/env python
"Use 2.x/3.x keywords args deletion with defaults"
import sys


def print3(*args, **kwargs):
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', '\n')
    file = kwargs.pop('file', sys.stdout)
    if kwargs:
        raise TypeError('extra keyword %s' % kwargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
