def Dayso_2cs(n):
    res = []
    for i in range(0, len(n)-1, 2):
        res.append(n[i]*10 + n[i+1])
    return sorted(list(set(res)))

n = [int(i) for i in list(input())]
print(*Dayso_2cs(n))