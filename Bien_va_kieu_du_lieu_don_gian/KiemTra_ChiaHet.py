def Ktra (L, R, n):
    M = (L+R)//2
    if L==M:
        for i in range(2, n+1):
            if L%i==0: return 0
        return 1
    return Ktra (L, M, n) + Ktra (M, R, n)
while 1:
    str = input()
    if str=="-1": break
    L, R = map(int, str.split())
    n = int(input())
    print(Ktra(L, R+1, n)) #R+1 vì đoạn [L,R], trong code return sang trái nên thiếu mất số R

# PYKT038 KIỂM TRA CHIA HẾT

# Cho ba số nguyên dương L, R và N. Viết chương trình đếm số lượng các số thỏa mãn cả hai điều kiện:

# Nằm trong đoạn [L, R].
# Không chia hết cho bất kỳ số nào trong đoạn [2, N].
# Input

# Với mỗi bộ test:

# Dòng đầu gồm 2 số nguyên dương L, R (1 ≤ L, R ≤ 1018).
# Dòng thứ 2 chứa số nguyên dương N (2 ≤ N ≤ 50).
# Input kết thúc với một dòng chứa số nguyên -1.

# Output

# Với mỗi bộ test, in ra kết quả trong một dòng.


# Input
# 1 10
# 10
# 2001 2309
# 50
# 34 2003
# 50
# -1
# Output

# 1

# 40

# 289