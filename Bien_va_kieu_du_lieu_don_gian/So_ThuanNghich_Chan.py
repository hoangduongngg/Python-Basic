def SoThuanNghich_Chan (n):
    n = str(n)
    if (n!=n[::-1] or len(n)%2): return 0
    for i in set(int(j) for j in list(n)):
        if i%2: return 0
    return 1

def Check(n):
    res = []
    for i in range(10, n):
        if SoThuanNghich_Chan(i): res.append(i)
    print(*res)
    
t = int(input())
while t>0:
    Check(int(input()))
    t-=1

# PY01043 SỐ THUẬN NGHỊCH CHẴN

# Cho số nguyên dương N không quá 6 chữ số.

# Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:

# N là số thuận nghịch
# Tất cả các chữ số của N đều chẵn
# Số chữ số của N cũng là một số chẵn
# Input

# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

# Output

# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.


# Input


# 2
# 30
# 100
# Output

# 22

# 22 44 66 88