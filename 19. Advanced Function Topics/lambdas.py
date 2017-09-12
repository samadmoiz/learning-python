def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

acts = knights()

msg = acts('Robin')

print(msg)

# Why use lambda
# lambda is commonly use to code 'jump tables' which are list and dictionaries

L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))

key = 'got'
print({'already': (lambda: 2 + 2),
       'got': (lambda: 2 * 4),
       'one': (lambda: 2 ** 6)}[key]())

# Obfuscate (unclear) Your Python Code
lower = (lambda x, y: x if x < y else y)
lower('aa', 'bb')

import sys
showall = lambda x: list(map(sys.stdout.write, x))

showall = lambda x: [sys.stdout.write(line) for line in x]

showall = lambda x: [print(line, end='') for line in x] # 3.x

showall = lambda x: print(*x, sep='', end='')
