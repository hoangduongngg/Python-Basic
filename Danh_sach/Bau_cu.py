def Bau_cu(a,n,m):
    b = []
    for i in range(1,m+1):
        b.append([i, a.count(i)])
    b = sorted(b, key = lambda k:(-k[1], k[0]))

    print(b)
    Max = b[0][1]
    for i in b:
        if i[1] <Max:
            return i[0]
    return -1

def Xuly(a,n,m):
    if Bau_cu(a,n,m)==-1:
        print("NONE")
    else:
        print(Bau_cu(a,n,m))

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
Xuly(a,n,m)

# Input

# 10 4
# 2 3 1 2 3 4 1 2 3 2

# 10 4
# 2 3 1 2 3 1 1 2 3 2
# Output

# 3

# Input

# 8 4
# 1 2 3 4 4 3 2 1

# Output

# NONE