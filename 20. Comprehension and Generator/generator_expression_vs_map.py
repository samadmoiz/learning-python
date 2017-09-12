import logging
import sys

list(map(abs, (-1, -2, 3, 4)))  # Map function on tuple

list(abs(x) for x in (-1, -2, 3, 4))  # Generator expression

list(map(lambda x: x * 2, (1, 2, 3, 4)))  # Nonfunction case

list(x * 2 for x in (1, 2, 3, 4))  # Simpler as generator

# case like text-processing

line = 'aaa,bbb,ccc'
a = ''.join([x.upper() for x in line.split(',')])  # Make a pointless list

b = ''.join(x.upper() for x in line.split(','))  # Generates result

c = ''.join(map(str.upper, line.split(',')))  # Generates result

# nested
d = [x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]  # nested comprehension

e = list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4))))  # nested map

f = list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4)))  # nested generator

import math

# nested combination
g = list(map(math.sqrt, (x ** 2 for x in range(4))))

# nested gone bad
list(map(abs, map(abs, map(abs, (-1, 0, 1)))))

list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1))))


# Flat is better than nested
list(abs(x) for x in range(-4, 4))

list(math.sqrt(x ** 2) for x in range(4))

list(abs(x) for x in (-1, 0, 1))
