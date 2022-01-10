def Ktra_SoDep (n):
    a = list(n)
    if (len(set(a))!=2):
        return 0
    for i in range(0, len(a)-1):
        if a[i]==a[i+1]: return 0
    return 1
def Check(n):
    if Ktra_SoDep(n):
        print("YES")
    else:
        print("NO")

t = int(input())
while t>0:
    Check(input())
    t-=1

# PY01039 KIỂM TRA SỐ ĐẸP

# Bài làm tốt nhất
# Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau và các chữ số ở cách nhau 2 vị trí đều bằng nhau. Ví dụ: 121, 1313131, 5656 …

# Viết chương trình kiểm tra một số có phải số đẹp hay không?

# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test ghi một số nguyên dương N (lớn hơn 10 và có không quá 18 chữ số) trên một dòng.

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Input

# 3
# 12121212
# 343433
# 78789989
# Output

# YES

# NO

# NO