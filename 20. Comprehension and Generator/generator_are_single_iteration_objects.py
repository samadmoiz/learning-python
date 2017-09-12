G = (x * 4 for x in 'SPAM')

I1, I2 = iter(G), iter(G)

next(I1)
# SSSS
next(I1)
# PPPP

next(I2)
# AAAA
next(I2)
# MMMM

next(I1)
# StopIteration

# same goes for generator function

def timefours(S):
    for c in S:
        yield c * 4

G = timefours("SPAM")

I1, I2 = iter(G), iter(G)

next(I1)
# SSSS

# list take the whole generator
list(I1)
# ["PPPP", "AAAA", "MMMM"]

next(I2)
# StopIteration

# multiple iteraotr from list
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

next(I1)
# 1
next(I2)
# 1

# above problem solve if generator mayy be limited
G = (x * 4 for x in 'SPAM')

L = list(G)
I1, I2 = iter(L), iter(L)
