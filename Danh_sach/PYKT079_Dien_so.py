def DienSo (a):
    n, L,R = len(a), min(a), max(a)
    res = 0
    for i in range(L,R+1):
        if i not in a: res+=1


    print(res)

t = int(input())
while t>0:
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    DienSo (a)
    t-=1

# In
# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3

# Out
# 1
# 0