def Diem_TB(a,n):
    Max, Min = max(a), min(a)
    for i in a:
        if i==Max or i ==Min:
            a.remove(i)
    return sum(i for i in a)/len(a)


n = int (input())
a = [float (i) for i in input().split()]
print(round(Diem_TB(a,n), 2))
