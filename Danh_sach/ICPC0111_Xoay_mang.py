def Xoay_mang(n,d,a):
    for i in range(d, n):
        print(a[i], end= " ")
    for i in range(0,d):
        print (a[i], end= " ")
    print()

t= int(input())
while t>0:
    n,d = map(int, input().split())
    a = input().split()
    Xoay_mang(n,d,a)
    t-=1

# Input:

# 2
# 5 2
# 1 2 3 4 5 
# 10 3
# 2 4 6 8 10 12 14 16 18 20
# Output:

# 3 4 5 1 2
# 8 10 12 14 16 18 20 2 4 6