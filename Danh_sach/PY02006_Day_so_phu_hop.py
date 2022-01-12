def DaySo_PhuHop(n,a,b):
    for i in range(0,n):
        if a[i]>b[i]:
            return 0
    return 1

def Check (n,a,b):
    if DaySo_PhuHop(n,a,b):
        print("YES")
    else:
        print("NO")
t = int (input())

while t>0:
    n = int (input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    Check(n,a,b)
    t-=1

# PY02006 DÃY SỐ PHÙ HỢP

# Cho hai dãy số A[] và B[] có cùng N phần tử. Dãy số A[] được gọi là phù hợp với dãy số B[] khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A[] và B[] sao cho phần tử thứ i của A[] nhỏ hơn hoặc bằng phần tử thứ i của mảng B[] (với tất cả vị trí trong dãy).

# Hãy xác định hai dãy số A[] và B[] có phù hợp với nhau hay không?

 

# Input:

# Dòng đầu tiên đưa vào số lượng bộ test T (T≤100).

# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 3 phần: phần thứ nhất là số N; phần thứ hai là N số của A[]; phần thứ 3 là N số của B[].

# (1≤N≤100, 0≤A[i], B[i]≤1000)

# Output:

# Đưa ra kết quả mỗi test theo từng dòng. Kết quả “YES” nếu A[] phù hợp với B[], ngược lại đưa ra “NO”.

 

# Ví dụ:

# Input:


# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84 
# Output:

# YES

# NO
 