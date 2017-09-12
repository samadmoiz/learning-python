#!/usr/bin/env python3


"""
def tester(start):
    state = start  # Referencing nonlocals works normally

    def nested(label):
        print(label, state)  # Remembers state in enclosing scope

    return nested

F = tester(0)
F('spam') # 0
F('ham') # 0
"""

"""
def tester(start):
    state = start  # Referencing nonlocals works normally

    def nested(label):
        print(label, state)  # Remembers state in enclosing scope
        state += 1  # cannot change by default

    return nested

F = tester(0)
F('spam') # UnboundLocalError
"""


def tester(start):
    state = start  # Referencing nonlocals works normally

    def nested(label):
        nonlocal state
        print(label, state)  # Remembers state in enclosing scope
        state += 1

    return nested

F = tester(0)
F('spam')
F('ham')
F('eggs')

G = tester(42)
G('spam')
G('ham')
G('eggs')

F('bacon')


# Boundary Cases
"""
def tester(start):
    def nested(label):
        nonlocal state # Nonlocals must already exist in enclosing def!
        state = 0
        print(label, state)
    return nested
# SyntaxError: no binding for nonlocal 'state' found

def tester(start):
    def nested(label):
        global state # Globals don't have to exist yet when declared
        state = 0 # This creates the name in the module now
        print(label, state)
    return nested

spam = 99
def tester():
    def nested():
        nonlocal spam # Must be in a def, not the module!
        print('Current=', spam)
        spam += 1
    return nested
# SyntaxError: no binding for nonlocal 'spam' found
"""
