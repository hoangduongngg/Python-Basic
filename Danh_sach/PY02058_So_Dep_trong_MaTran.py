def SoDep_MaTran(a):
    n = len(a)
    m = len(a[0])
    Max = max(max(a[i]) for i in range(0,n))
    Min = min(min(a[i]) for i in range(0,n))
    SoDep = Max - Min

    flag = 0
    for i in range(0,n):
        if SoDep in a[i]:
            flag = 1
            break

    if flag == 0:
        print("NOT FOUND")
    else:
        print(SoDep)
        for i in range(0,n):
            for j in range(0,m):
                if a[i][j]==SoDep:
                    print(f"Vi tri [{i}][{j}]")

n, m = map(int, input().split())
a = []
a.index
for i in range(0,n):
    a.append([int(i) for i in input().split()])
SoDep_MaTran(a)

# PY02058 SỐ ĐẸP TRONG MA TRẬN

# Bài làm tốt nhất
# Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.

# Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cách giữa số lớn nhất và số nhỏ nhất của ma trận.

# Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.

# Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?

# Input

# Dòng đầu ghi hai số N và M (1 < N, M < 50)

# Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

# Output

# Ghi ra giá trị bằng số may mắn nếu tìm được. Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

# Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND

# Ví dụ

# Input


# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77

# Output

# 67

# Vi tri [2][1]

# Vi tri [3][3]