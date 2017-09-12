def tracer(func, *pargs, **kwargs):
    print('calling:', func.__name__)
    return func(*pargs, **kwargs)


def func(a, b, c, d):
    return a + b + c + d


print(tracer(func, 1, 2, c=3, d=4))
