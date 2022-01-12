def Tich_lon_nhat(a):
    a = sorted(a)
    return max(a[0]*a[1], a[0]*a[1]*a[2], a[-2]*a[-1], a[-3]*a[-2]*a[-1])

n = int(input())
a = [int(i) for i in input().split()]
print(Tich_lon_nhat(a))

# Input

# 6
# 5 10 -2 3 5 2

# Output

# 250
