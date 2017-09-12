import sys
import timer2

reps = 10000
repslist = list(range(reps))  # Hoist out, list in both 2.X/3.X


def run1():
    def f(x):
        return x
    return [f(x) for x in 'spam' * 2500]

def run2():
    def f(x):
        return x
    res = []
    for x in 'spam' * 2500:
        res.append(f(x))
    return res

def run3():
    def f(x):
        return x
    return list(map(f, 'spam' * 2500))

def run4():
    def f(x):
        return x
    return list(f(x) for x in 'spam' * 2500)


print(sys.version)

for test in (run1, run2, run3, run4):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)


    # (total, result) = timer2.bestoftotal(test)
    # (total, result) = timer2.bestoftotal(test, _reps1=5)
    # (total, result) = timer2.total(test, _reps=1000)
    # (bestof, (total, result)) = timer2.bestof(timer2.total, test, n_reps=5)

    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, total, result[0], result[-1]))
