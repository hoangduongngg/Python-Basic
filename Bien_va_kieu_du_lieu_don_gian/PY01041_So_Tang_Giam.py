def Check_SoTangGiam(n):
    a = [int(i) for i in list(n)]
    x = 0 #vi tri tang giam
    for i in range(0, len(a)-1):
        if a[i]>a[i+1]:
            x = i
            break
        if a[i]==a[i+1]: return 0
    if x==len(a)-1 or x==0: return 0
    for i in range(x, len(a)-1):
        if a[i]<=a[i+1]: return 0

    return 1
def Check(n):
    if Check_SoTangGiam(n): print("YES")
    else: print("NO")

t = int (input())
while t>0:
    Check(input())
    t-=1

# PY01041 SỐ TĂNG GIẢM

# Bài làm tốt nhất
# Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:

# Có từ 3 chữ số trở lên
# Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt) còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
# Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test viết trên một dòng số nguyên dương N không quá 18 chữ số

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
# Input


# 3
# 12342
# 23342
# 5678961
# Ouput

# YES

# NO

# YES