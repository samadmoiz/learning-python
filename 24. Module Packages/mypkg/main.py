# import string  # absolute
# from string import name  # absolute as well
# from . import string # relative
# from .string import name1, name2
# from .. import string  # relative parent sibling

from mypkg import string  # absolute search current string.py
# from . import string # relative

print(string.name1)
print(string.name2)
print(string.name3)
print(string.hello)
