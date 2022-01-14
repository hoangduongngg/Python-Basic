import math
import re
mod = pow(10,9) + 7
def POW (x, n):
    if n==0: return 1
    if n==1: return x%mod
    return (x%mod * POW(x%mod, n-1)) %mod

def Xuly(n):
    s = str(POW(3 + math.sqrt(5), n)) + '.'
    # print(s)
    x = s.index('.')
    if x<3:
        res = (3-x)*'0' + s[:x]
    else:
        res = s[x-3:x]
    return res

t = int(input())
for i in range(1, t+1):
    print(f"Case #{i}: {Xuly(int(input()))}")

# Lỗi đang gặp: Không xử lý đc số lớn 
# Idea: Chuyển sang str

# PYKT13006 TÌM CHỮ SỐ

# Bài làm tốt nhất
# Hãy tìm 3 chữ số đầu tiên trước dấu phẩy của số (3+sqrt(5))^n.

# Ví dụ:

# Với n = 5, (3+sqrt(5))^5 = 3935.73982… Đáp số là 935.

# Với n = 2, (3+sqrt(5))^2 = 27.4164079… Đáp số là 027.

# Input:

# Dòng đầu tiên là số lượng bộ test T (T ≤ 100).

# Mỗi test gồm một số nguyên n (n ≤ 2 000 000 000).

# Output: 

# Với mỗi test in ra STT và đáp án tìm được. In ra đủ 3 chữ số như test ví dụ (n = 2, in ra 027).

 

# Ví dụ:

# Input

# 2
# 5
# 2

# Output

# Case #1: 935
# Case #2: 027