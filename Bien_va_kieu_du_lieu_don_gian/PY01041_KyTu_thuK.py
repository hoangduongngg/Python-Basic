import math
def KyThu_thuK (n,k):
    x = math.pow(2, n-1)    #vi tri chinh giua
    if k==x:
        return chr(ord('A') + n-1)
    elif k<x:
        return KyThu_thuK(n-1, k)
    else:
        return KyThu_thuK(n-1, k-x)
    return 'A'

t = int(input())
while t>0:
    n,k = map(int, input().split())
    print(KyThu_thuK(n,k))
    t-=1

# Idea: Đệ quy
# PY01041 KÝ TỰ THỨ K

# Xâu ký tự S được tạo ra bằng cách bổ sung dần các ký tự chữ cái Tiếng Anh in hoa như sau.

# Bước 1: Chỉ có chữ cái A
# Bước 2: Thêm chữ cái B vào giữa 2 chữ A => S = "ABA"
# Bước 3: Thêm chữ cái C vào giữa 2 xâu đã có ở bước 2: S = "ABACABA"
# Cứ như vậy cho đến bước thứ N (0 < N < 26)

# Hãy xác định ký tự thứ K trong bước biến đổi thứ N là chữ cái gì?

# Input:

# Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
# Mỗi test gồm số nguyên dương N và K (1 ≤ N ≤ 25, 1 ≤ K ≤ 2^N - 1).
# Output: 

# Với mỗi test, in ra đáp án trên một dòng.

# Input:

# 2
# 3 2
# 4 8

 
# Output

# B

# D