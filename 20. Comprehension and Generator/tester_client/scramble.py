def scramble(seq):
    for i in range(len(seq)):
        yield seq[1:] + seq[:1]
