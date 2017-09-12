#!/usr/bin/env python3

"""
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
# a = 1, b = (2, ), c = 3

kwonly(a=1, c=3)
# a = 1, b = (), c = 3

# print(kwonly(1, 2, 3))
# ERROR
"""


# using the * character we can force later arguments to be keyword only
"""
def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c=3, b=2)

kwonly(c=3, b=2, a=1)

kwonly(1, 2, 3)
# ERROR

kwonly(1)
# ERROR"""


# You can still use default keyword-only arguments, even though they appear
# after the * in the function header, in this example `a` can be positional or
# named and b and c can be optional and keyword-only arguments
"""def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1)

kwonly(1, c=3)

kwonly(a=1)

kwonly(a=1, c=3, b=2)

kwonly(1, 2)
#ERROR"""


def kwonly(a, *, b, c='spam'):
    print(a, b, c)

kwonly(1, b='eggs')
# a = 1, b = eggs, c = 'spam'

kwonly(1, c='eggs')
# ERROR: b is required

kwonly(1, 2)
# ERROR: b must be keyword-only argument

