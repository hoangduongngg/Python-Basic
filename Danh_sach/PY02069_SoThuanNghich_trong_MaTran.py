def So_ThuanNghich(n):
    n = str(n)
    if len(n)<2: return 0
    if n != n[::-1]: return 0
    return 1

def STN_Max_MaTran(a):
    n = len(a)
    m = len(a[0])

    STN_Max = 0
    for i in range(0,n):
        for j in range(0,m):
            if So_ThuanNghich(a[i][j]) and a[i][j]>STN_Max:
                STN_Max = a[i][j]

    if STN_Max == 0:
        print("NOT FOUND")
    else:
        print(STN_Max)
        for i in range(0,n):
            for j in range(0,m):
                if a[i][j]==STN_Max:
                    print(f"Vi tri [{i}][{j}]")

n, m = map(int, input().split())
a = []
for i in range(0,n):
    a.append([int(i) for i in input().split()])
STN_Max_MaTran(a)

# PY02069 SỐ THUẬN NGHỊCHTRONG MA TRẬN

# Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.

# Một số được coi là thuận nghịch nếu có từ 2 chữ số trở lên và nếu viết theo thứ tự ngược lại giá trị vẫn không thay đổi so với giá trị ban đầu. Ví dụ: 99, 121, 1331

# Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.

# Input

# Dòng đầu ghi hai số N và M (1 < N, M < 50)

# Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

# Output

# Ghi ra giá trị của số thuận nghịch lớn nhất. Sau đó lần lượt là các vị trí của số thuận nghịch lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

# Nếu không tìm thấy số thuận nghịch nào thì ghi ra NOT FOUND

# Ví dụ

# Input


# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77
# .Output

# 77

# Vi tri [0][2]

# Vi tri [3][1]

# Vi tri [5][2]

# Vi tri [5][3]