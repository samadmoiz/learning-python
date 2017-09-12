#!/usr/bin/env python3

import builtins


"""def makeopen(id):
    original = builtins.open

    def custom(*kargs, **pargs):
        print('Custom open call %r' % id, kargs, pargs)
        return original(*kargs, **pargs)
    builtins.open = custom"""

"""
# My Custom Example
def hello():
    pass

def make(id):
    global hello
    original = hello

    def custom():
        print('Custom open call %r' % id)
        return original()

    hello = custom

make('spam')
# hello()
make('jam')
hello()"""


class makeopen:

    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self

    def __call__(self, *kargs, **pargs):
        print('Custom open call %r' % self.id)
        return self.original(*kargs, **pargs)
