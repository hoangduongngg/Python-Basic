def SapXep(a):
    chan = []
    le = []
    for i in a:
        if i%2==0: chan.append(i)
        else: le.append(i)
    
    chan = sorted(chan, reverse=True)
    le = sorted(le)

    res = []
    for i in a:
        if i%2==0:
            res.append(chan[-1])
            chan.pop()
        else:
            res.append(le[-1])
            le.pop()
    print(*res)

n = int(input())
a = []
while len(a) <n:
    a.extend(int(i) for i in input().split())
SapXep(a)


# 10
# 1 2 3 4 5 6 7 7 9 6

# 9 2 7 4 7 6 5 3 1 6

