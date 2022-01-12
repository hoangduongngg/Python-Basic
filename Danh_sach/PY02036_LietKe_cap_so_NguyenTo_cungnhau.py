import math
def LietKe (a):
    a = sorted(int(i) for i in a.split())
    n = len(a)
    for i in range(0,n-1):
        for j in range(i+1, n):
            if math.gcd(a[i], a[j]) == 1:
                print(a[i], a[j])

n = int(input())
LietKe(input())
# 5
# 3 7 9 6 13