trace = lambda x: None               # or print
visit = lambda x: print(x, end=', ')

# [1, 2, [3, 4, [5, 6]], [[[7]]]]


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))


# see sumtree2.py
# Recursion versus queues and stack
def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot


def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot


def sumtree(L):
    tot = 0
    levels = [L]
    while levels:
        trace(levels)
        front = levels.pop(0)                    # Fetch/delete front path
        for x in front:
            if not isinstance(x, list):
                tot += x                         # Add numbers directly
                visit(x)
            else:
                levels.append(x)                 # Push/schedule nested lists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)
print('-'*40)
