def f(a, b, c):
    print('%s, %s and %s' % (a, b, c))

f(0, 1, 2)

f(*range(3))

f(*(i**2 for i in range(3)))
