#!/usr/bin/env python3
# Why nonlocal? State Retention Option
"""
Summary:
global, nonlocal, class, function attribute all offer changeable
state-retention option
Globals support only single-copy shared data; nonlocals can be changed in 3.X
only; classes require a basic knowledge of OOP; and both classes and function
attributes provide portable solutions that allow state to be accessed directly
from outside the stateful callable object itself.
"""

# State with nonlocal: 3.x only
"""
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')
F('ham')

G = tester(42)
G('moiz')
G('samad')
F('eggs')
"""

# Alternative for 2.x
# State with Global: A Single Copy Only
"""
def tester(start):
    global state
    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested
F = tester(0)
F('spam')
F('ham')

G = tester(42)  # Problem: global state reset when each call tester
G('moiz')
G('samad')
F('eggs')
"""

# State with Class: Explicit Attributes (Preview)
"""
class tester:
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1

F = tester(0)
F.nested('spam')
F.nested('ham')

G = tester(42)
G.nested('moiz')
G.nested('samad')
F.nested('eggs')
"""

# Callable
"""
class tester:
    def __init__(self, start):
        self.state = start

    def __call__(self, label):
        print(label, self.state)
        self.state += 1
F = tester(0)
F('spam')
F('ham')

G = tester(42)
G('moiz')
G('samad')
F('eggs')
"""

# State with Function Attributes 3.x and 2.x
"""def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(0)
F('spam')
F('ham')

G = tester(42)
G('moiz')
G('samad')
F('eggs')

print(F.state)
print(G.state)
print(dir(F))"""

# State with mutables: Obscure ghost of Python past
"""def tester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1
    state = [start]
    return nested

F = tester(0)
F('spam')
F('ham')

G = tester(42)
G('moiz')
G('samad')
F('eggs')"""
