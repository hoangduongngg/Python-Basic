def Dthi_sao (dt):
    for i in dt.values():
        if len(i) == len(dt)-1:
            return 1
    return 0
def Check(dt):
    if Dthi_sao(dt): print("Yes")
    else: print("No")

n =int(input())
dt = {}
for i in range(1,n+1):
    dt[i] = []
    
for i in range(0,n-1):
    a,b = map(int, input().split())
    dt[a].append(b)
    dt[b].append(a)
Check(dt)

# PY03008 ĐỒ THỊ HÌNH SAO

# Bài làm tốt nhất
# Một đơn đồ thị vô hướng được gọi là Hình Sao nếu có một đỉnh có thể nối đến tất cả các đỉnh còn lại, còn các đỉnh khác thì không có cạnh nối với nhau.

# Cho mô tả một đơn đồ thị vô hướng N đỉnh với đúng N-1 cạnh. Hãy kiểm tra xem đồ thị đó có phải dạng Hình Sao hay không.

# Dữ liệu vào

# Dòng đầu tiên ghi số N là số đỉnh của đồ thị (1 ≤ N ≤ 105).
# N-1 dòng tiếp theo, mỗi dòng ghi ra một cặp (u,v) là cạnh của đồ thị. Dữ liệu đảm bảo u ≠ v.
# Kết quả

# Ghi ra trên một dòng chữ “Yes” nếu đồ thị là Hình Sao; chữ “No” trong trường hợp ngược lại.
# Ví dụ

# Input


# 5
# 1 2
# 1 3
# 1 4
# 1 5

# Output
# Yes