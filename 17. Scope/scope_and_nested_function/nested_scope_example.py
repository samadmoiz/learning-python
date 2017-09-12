X = 99  # Global scope name: not used


def f1():
    X = 88  # Enclosing def locals

    def f2():
        print(X)  # Reference made in nested def
    f2()


f1()  # print 88: enclosing def locals
