t = int(input())
a = [int(i) for i in input().split()]
res = [a[0]]
for i in range(1,len(a)):
    res.append(res[-1] + a[i])

Tich = 1
for i in res:
    Tich *= i
print(sum(res), Tich)

# 3
# 1 2 3