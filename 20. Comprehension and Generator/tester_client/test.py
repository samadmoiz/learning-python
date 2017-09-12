from scramble import scramble
from inter2 import intersect

def tester(func, items, trace=True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*args)))

tester(intersect, ('aaab', 'abbbc', 'cccab'), trace=False)
