import itertools
def Xuly(a,k):
    a = sorted(set(a))
    res = itertools.combinations(a,k) #tuple
    for i in res:
        print(*i)

n,k = map(int, input().split())
a = [int(i) for i in input().split()]

Xuly(a,k)

# PY01072 BÀI TOÁN TỔ HỢP

# Bài làm tốt nhất
# Cho dãy số A[] có N phần tử. Hãy liệt kê tất cả các tổ hợp chập K của tập các phần tử khác nhau trong A[]. Các tổ hợp cần liệt kê theo thứ tự từ điển (tức là trong mỗi tổ hợp thì giá trị từ nhỏ đến lớn, và tổ hợp sau lớn hơn tổ hợp trước).

# Input

# Dòng đầu ghi hai số N và K.

# Dòng thứ 2 ghi N số của mảng A[]. Các giá trị không quá 1000.

# Dữ liệu đảm bảo số phần tử khác nhau của A[] không quá 20 và K không quá 10.

# Output

# Ghi ra lần lượt các tổ hợp tìm được, mỗi tổ hợp trên một dòng.

# Ví dụ

# Input


# 8 3
# 2 4 4 3 5 1 3 4

# Output
# 1 2 3
# 1 2 4
# 1 2 5
# 1 3 4
# 1 3 5
# 1 4 5
# 2 3 4
# 2 3 5
# 2 4 5
# 3 4 5