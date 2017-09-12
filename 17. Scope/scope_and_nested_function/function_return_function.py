X = 99  # Global scope name: not used


def f1():
    X = 88  # Enclosing def locals

    def f2():
        print(X)  # Remember X in enclosing def scope

    return f2  # Return f2 but don't call it


action = f1()  # Make, return function
action()  # Call it now print 88
