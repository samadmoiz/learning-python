# keyword-only and named or postional argument must appear before **args
"""
def kwonly(a, **pargs, b, c):
    pass
"""

# **args cannot appear itself in the args list
"""
def kwonly(a, **, b, c):
    pass
"""

# correct
"""
def kwonly(a, b=3, **pargs):
    pass
"""


"""
def f(a, *b, c=6, **d):
    print("a = {} b = {} \nc = {} d = {}".format(a, b, c, d))

f(1, 2, 3, x=4, y=5)

# override default
f(1, 2, 3, x=4, y=5, c=7)

# anywhere
f(1, 2, 3, c=6, x=4, y=5)
"""

# keyword is not only here
"""
def f(a, c=6, *b, **d):
    print("a = {} b = {} \nc = {} d = {}".format(a, b, c, d))

f(1, 2, 3, x=4)
"""

# KW-only between * and **


def f(a, *b, c=6, **d):
    print("a = {} b = {} \nc = {} d = {}".format(a, b, c, d))

# kw-only args in call can be appear before or after *, but must appear before
# **args
f(1, *(2, 3), **dict(x=4, y=5))

f(1, *(2, 3), **dict(x=4, y=5), c=7)

f(1, *(2, 3), c=7, **dict(x=4, y=5))

f(1, c=7, *(2, 3), **dict(x=4, y=5))

f(1, *(2, 3), **dict(x=4, c=7, y=5))  # kw-only in **

# example
"""
def process(*a, notify=True):
    ...
process(a, b, c) # use default
process(a, b, notify=False) # override default
"""

