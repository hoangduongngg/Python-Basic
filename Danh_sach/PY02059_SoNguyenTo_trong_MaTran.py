def SNT(n):
    if n==2: return 1
    if n<2 or n%2==0: return 0
    i=3
    while i*i<=n:
        if n%i==0: return 0
        i+=2
    return 1

def SNT_Max_MaTran(a):
    n = len(a)
    m = len(a[0])

    SNT_Max = 0
    for i in range(0,n):
        for j in range(0,m):
            if SNT(a[i][j]) and a[i][j]>SNT_Max:
                SNT_Max = a[i][j]

    if SNT_Max == 0:
        print("NOT FOUND")
    else:
        print(SNT_Max)
        for i in range(0,n):
            for j in range(0,m):
                if a[i][j]==SNT_Max:
                    print(f"Vi tri [{i}][{j}]")

n, m = map(int, input().split())
a = []
a.index
for i in range(0,n):
    a.append([int(i) for i in input().split()])
SNT_Max_MaTran(a)

# PY02059 SỐ NGUYÊN TỐ TRONG MA TRẬN

# Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.

# Hãy tìm số nguyên tố lớn nhất trong ma trận và các vị trí có giá trị bằng số nguyên tố lớn nhất đó.

# Input

# Dòng đầu ghi hai số N và M (1 < N, M < 50)

# Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.

# Output

# Ghi ra giá trị của số nguyên tố lớn nhất. Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

# Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND


# Input


# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29

# Output

# 29

# Vi tri [2][1]

# Vi tri [3][0]

# Vi tri [5][3]