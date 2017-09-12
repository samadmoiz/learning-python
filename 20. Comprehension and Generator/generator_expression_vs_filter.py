line = 'aa bbb c'

a = ''.join(x for x in line.split() if len(x) > 1)  # generator with if

b = ''.join(filter(lambda x: len(x) > 1, line.split()))  # similer to filter

# adding proccessing steps to filter requires a map too

c = ''.join(x.upper() for x in line.split() if len(x) > 1)

d = ''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split())))

# statement equvilant
res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()


