import sys
import timer3

reps = 10000
repslist = list(range(reps))  # Hoist out, list in both 2.X/3.X


def forloop():
    res = []
    for i in repslist:
        res.append(abs(i))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))  # use list() here in 3.x only
    # return map(abs, repslist)


def genExp():
    return list(abs(x) for x in repslist)  # list required to force the result


def genFunc():
    def gen():
        for i in repslist:
            yield abs(i)
    return list(gen())  # list required to force the result

print(sys.version)

for test in (forloop, listComp, mapCall, genExp, genFunc):
    # (total, result) = timer3.total(test, _reps=1000)
    (total, result) = timer3.bestoftotal(test, _reps1=5, _reps=1000)
    # (total, result) = timer3.bestof(test, _reps=1000)
    # (best, (total, result)) = timer3.bestof(timer3.total, test, _reps=5)

    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, total, result[0], result[-1]))
