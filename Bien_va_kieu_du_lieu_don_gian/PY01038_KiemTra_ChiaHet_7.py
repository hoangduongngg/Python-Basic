def Ktra(n):
    if int(n)%7==0: return n
    t = 0
    while t<=1000:
        res = int(n) + int(n[::-1])
        if (res%7==0):
            return str(res)
        else:
            n = str(res)
        t+=1
    return -1

t = int(input())
while t>0:
    print(Ktra(input()))
    t-=1

# PY01038 KIỂM TRA CHIA HẾT CHO 7

# Cho một số nguyên dương N. Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.
# Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.
# Input:

# Dòng đầu ghi số bộ test (không quá 1000).

# Mỗi test ghi số N (1 ≤ N ≤ 1018)

# Output:

# Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. Hoặc số -1 nếu không thể tìm được đáp án.
# Input


# 5
# 1
# 2
# 3
# 4
# 999999
# Output

# 77

# 77

# 9447438

# 77

# 999999