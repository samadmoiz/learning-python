def intersects(seq1, seq2):
    "Order does not matter"
    set1 = set(seq1)
    set2 = set(seq2)
    return list(set1 & set2)


def intersect(seq1, seq2):
    "Order of first sequence"
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
