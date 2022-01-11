def ThongKe (a):
    n = len(a)
    m = len(a[0])
    res = 0
    b = [] #mang luu trọng số
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(0)
        b.append(row)

    for i in range(0,n):
        for j in range(0,m):
            if a[i][j] == '-1':
                # b[i][j] = -1
                for k in range(max(0, i-1), min(i+2, n)):
                    for l in range(max(0, j-1), min(j+2, m)):
                        # if b[k][l] == -1 :
                        #     res +=1
                        if b[k][l] ==0:
                            b[k][l] = int(a[k][l])
    for i in range(0,n):
        for j in range(0,m):
            if b[i][j] >0:
                res+=b[i][j]
    return res

n, m = map(int, input().split())
a = []
for i in range(0,n):
    a.append(input().split())
print(ThongKe(a))

# Idea: đánh dấu xung quanh bệnh nhân là flag =1, sau đó đếm 
# PYKT080 THỐNG KÊ DỊCH TỄ

# Trước diễn biến phức tạp của dịch bệnh, thành phố đang có chủ chương thống kê dịch tễ các trường hợp liên quan đến bệnh nhân mắc COVID-19.
# Thông tin về bệnh nhân được biểu diễn trên ma trận. Bạn hãy thực hiện thống kê nhanh các trường hợp có nguy cơ lây nhiễm. Nguyên tắc tính là đếm các trường hợp xung quanh bệnh nhân đã tiếp xúc (8 ô xung quanh).

# Input:

# Dòng đầu tiên là 2 số M, N là các số nguyên <= 100, cho biết kích thước của ma trận.
# Tiếp theo là ma trận M x N, các số nguyên A[i][j] có giá trị < 10. Vị trí của mỗi bệnh nhân được đánh số -1. Các ô mang giá trị >= 0 thể hiện số trường hợp có nguy cơ lây nhiễm (không tính các bệnh nhân).

# Output:

# Tổng số các ca có nguy cơ lây nhiễm trên toàn thành phố.

# Input:


# 4 4
# -1 1 0 1
# 2 -1 -1 5
# 0 0 -1 0
# 1 0 2 3
# Output:

#  8


# 4 4
# 1 1 0 1 
# 2 -1 4 5 
# 0 0 -1 0 
# 1 0 2 1