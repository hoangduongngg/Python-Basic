import itertools
def HoanVi (s):
    res = itertools.permutations(s)
    for i in res:
        print(*i, sep = "")

HoanVi(input())

# XYZ

# ----

# XYZ

# XZY

# YXZ

# YZX

# ZXY

# ZYX