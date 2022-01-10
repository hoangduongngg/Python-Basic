import math
def SNT(n):
    if n==2: return 1
    if (n<2 or n%2==0): return 0
    i=3
    while i*i<=n:
        if n%i==0: return 0
        i+=2
    return 1

def Ktra_UuThe (n):
    # n: string 
    if not SNT(len(n)): return 0
    x = 0 #so luong cso ngto
    for i in n:
        if SNT(int(i)): x+=1
    if x*2<=len(n): return 0

    return 1

def Check(n):
    if Ktra_UuThe(n):
        print("YES")
    else:
        print("NO")


t = int (input())
while t>0:
    n = input()
    Check(n)
    t-=1


# PY01049 CHỮ SỐ NGUYÊN TỐ
# Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:

# Số chữ số của nó là một số nguyên tố
# Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
# Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

# Input

# Dòng đầu ghi số bộ test, không quá 20.
# Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
# Input
# 3
# 1234567
# 22334455667
# 23400300489898989

# Output
# YES
# YES
# NO