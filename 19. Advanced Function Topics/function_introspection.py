def func(a):
    b = "spam"
    return a * b

func.__name__

dir(func)

func.__code__

dir(func.__code__)

func.__code__.co_varnames

func.__code__.co_argcount

# Tool writers can make use of such information to manage functions
