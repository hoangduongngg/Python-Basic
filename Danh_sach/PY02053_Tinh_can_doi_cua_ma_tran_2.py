def Do_chech_lech(a,n):
    sum_tren = sum_duoi = 0
    for i in range(0,n):
        for j in range(0,n-1-i):
            sum_tren += a[i][j]
        for k in range(0,i):
            sum_duoi += a[i][n-1-k]
    return abs (sum_tren - sum_duoi)

n = int (input())
a = []
for i in range(0,n):
    a.append([int(x) for x in input().split()])
k = int (input())

if Do_chech_lech(a,n)>k:
    print("NO")
else:
    print("YES")
print(Do_chech_lech(a,n))