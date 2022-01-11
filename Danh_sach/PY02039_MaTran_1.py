def Tong_DuongCheo_Chinh (a):
    # a[i] = a[j]
    res = 0
    for i in range(0,len(a)):
        res += a[i][i]
    return res
def Tong_Nua_Tren (a):
    res = 0
    for i in range(0,len(a)):
        for j in range(i+1, len(a)):
            res += a[i][j]
    return res

def Tong_Ma_Tran (a):
    res = 0
    for i in range(0, len(a)):
        res += sum(a[i])
    return res
def Tong_Nua_Duoi (a):
    return Tong_Ma_Tran(a) - Tong_Nua_Tren(a) - Tong_DuongCheo_Chinh(a)
def Ktra_CanDoi (a,k):

    ChechLech = abs(Tong_Nua_Tren(a) - Tong_Nua_Duoi(a))
    
    if ChechLech<=k: print("YES")
    else: print("NO")
    print(ChechLech)
    
n = int(input())
a = []
for i in range(0,n):
    a.append([int(i) for i in input().split()])
k = int(input())
Ktra_CanDoi(a,k)

# PY02039 MA TRẬN - 1
# Giống bài PY02052 - Tính cân đối ma trận 1

# Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.
# Với đường chéo chính, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo chính (không tính các phần tử nằm trên đường chéo chính).
# Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy tổng giá trị các phần tử ở nửa trên trừ đi tổng giá trị các phần tử ở nửa dưới.
# Nhập thêm một giá trị K gọi là ngưỡng cân đối của ma trận.  
# Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.
# Hãy xác định độ chênh lệch và tính cân đối của ma trận.

# Input
# Dòng đầu ghi số N (2 < N < 50)
# N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.
# Dòng cuối ghi số K (0 < K <100)

# Output

# Dòng đầu ghi chữ YES hoặc NO
# Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

# Input

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5

# Output

# YES
# 3