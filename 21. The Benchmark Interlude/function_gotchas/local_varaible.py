# local variable are detected statically
x = 99
def f():
    print(x)
f()


def f():
    print(x)
    x = 22
f()
# error: x is referenced before asigned

# even if x is define in global scope
x = 99
def f():
    print(x)
    x = 22
f()
# error: x is referenced before asigned

# but x also changes if you declare it globa statement
x = 99
def f():
    print(x)
    x = 88
f()
# 99
# x == 88

# if you really need to print global and then set local name
x = 99
def f():
    import __main__
    print(__main__.x)
    x = 88
    print(x)

f()
