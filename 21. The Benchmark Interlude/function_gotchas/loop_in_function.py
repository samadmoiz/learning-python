def f():
    l = []
    for x in range(5):
        l.append(lambda: x ** 2)
    return l

l = f()
l[0]()  # 25
l[1]()  # 25
l[1]()  # 25


def f():
    l = []
    for x in range(5):
        l.append(lambda i=x: i ** 2)
    return l

l = f()
l[0]()  # 0
l[1]()  # 1
l[2]()  # 4


list = 'hello'
dict = 'yello'
