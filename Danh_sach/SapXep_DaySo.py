def SapXep_DaySo (n,m,a):
    # a = []
    a.insert(a.index(max(a)), m)

    print(a)

t = int(input())
while t>0:
    n, m  = map(int, input().split())
    a = [int(i) for i in input().split()]
    SapXep_DaySo(n,m,a)
    t-=1

# PYKT078 SẮP XẾP DÃY SỐ

# Cho dãy số nguyên x1 , x2 , … ,x  và số nguyên m

# - Tìm giá trị lớn nhất của dãy số.

# - Chèn m vào trước vị trí đầu tiên có giá trị bằng giá trị lớn nhất.

# - Sắp xếp lại dãy số sau chèn sao cho phần tử âm về đầu dãy, phần tử dương và bằng 0 về cuối dãy sao cho trật tự các phần tử không thay đổi.

# Input:

# Dòng đầu tiên cho T là số lượng bộ test.

# Mỗi bộ test bao gồm hai dòng, dòng 1 cho số n < 1000 là số lượng phần tử và số m sao cho  -109 < m < 109.

# Dòng thứ 2 của bộ test bao gồm m số nguyên -109 < Xi < 109

# Output:

# In ra kết quả theo từng dòng

# Input:


# 1
# 5 3
# -1 2 3 4 -1

# Output:

# -1 -1 2 3 3 4