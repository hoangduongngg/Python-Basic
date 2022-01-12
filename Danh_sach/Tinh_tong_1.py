import math
def Tinh_tong (n,k):
    # mod = pow(10,9) + 7
    if n<=1: return n
    return pow(n, k) + Tinh_tong(n-1, k)

t = int(input())
while t>0:
    n, k = map(int, input().split())
    print(Tinh_tong(n,k))
    t-=1

# PYKT13009 TÍNH TỔNG 1

# Cho 2 số nguyên n và K. Hãy tính giá trị biểu thức theo modulo 109+7.

# Input:

# Dòng đầu tiên là số lượng bộ test T (T ≤ 20).

# Mỗi test gồm 2 số nguyên dương n và K (n ≤ 109, K ≤ 50).

# Output: 

# Với mỗi test, in ra đáp án tìm được theo modulo 109 + 7.


# Input:


# 3
# 1 1
# 4 2
# 10 3

# Output

# 1

# 30

# 3025