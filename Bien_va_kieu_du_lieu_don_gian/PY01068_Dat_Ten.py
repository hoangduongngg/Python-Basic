import itertools
def To_Hop(a,k):
    a = sorted(set(a))
    res = itertools.combinations(a,k)
    for i in res:
        print(*i)

n,k = map(int, input().split())
a = input().split()
To_Hop(a,k)

# 6 2
# DONG TAY NAM BAC TAY BAC


# BAC DONG
# BAC NAM
# BAC TAY
# DONG NAM
# DONG TAY
# NAM TAY