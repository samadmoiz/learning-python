# following code will repeat each character 4 times
G = (c * 4 for c in 'SPAM')
I = iter(G)  # Iterates manually
print(next(I))
print(next(I))

print(list(G))  # Iterates automatically

def timefours(S):
    for c in S:
        yield c * 4

G = timefours('spam')
print(list(G))

line = 'aa bbb c'

''.join(x.upper() for x in line.split() if len(x) > 1)

def gensub(line):
    for x in line.split():
        if len(x) > 1:
            yield x.upper()

''.join(gensub(line))
