def Doi_Co_So (n, k):
    res = ""
    while n/k!=0:
        if n%k<10:
            res+=str(n%k)
        else:
            res+= chr(ord('A') + n%k-10)
        n = int(n/k)
    return res[::-1]

t = int(input())
while t>0:
    n, k = map(int, input().split())
    print (Doi_Co_So(n,k))
    t-=1

# PYKT037 ĐỔI CƠ SỐ

# Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).

# Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. Trong đó N không quá 100.000, 2 ≤ b ≤ 36.

# Input

# Dòng đầu ghi số bộ test, không quá 10.

# Mỗi bộ test ghi 2 số N và b.

# Nlà một số nguyên dương N trong cơ số 10, không quá 100.000.  2 ≤ b ≤ 36

# Output

# Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.


# Input

# 3
# 10 2
# 2021 2

# 31 16
# Ouput

# 1010
# 11111100101
# 1F