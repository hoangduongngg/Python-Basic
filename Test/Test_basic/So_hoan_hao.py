import math
def So_hoan_hao(n):
    sum = 0
    for i in range(1, (n//2)+1):
        if n%i==0:
            sum+=i
    if sum == n:
        return 1
    else:
        return 0

n = int (input())
if So_hoan_hao(n):
    print("YES")
else:
    print("NO")