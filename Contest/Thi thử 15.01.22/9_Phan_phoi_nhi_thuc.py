from decimal import Decimal
import math
def PhanBoNhiThuc (n,p,x):
    res = math.comb(n,x) * pow(p,x) * pow(1-p, n-x)
    return '%.6f'%res

t = int(input())
while t>0:
    a = input().split() #n,p,x - 4 0.45 3
    print(PhanBoNhiThuc (int(a[0]) , Decimal(a[1]), int(a[2])))
    t-=1

# Vấn đề: bài này test cứ sao sao ấy. 
# rõ nói 3 số là n,p,x mà 4>3 thì không thỏa mãn rồi
# còn nếu đổi lại thành 4 0.45 3 thì cũng k ra giống output=))

# PHÂN PHỐI NHỊ THỨC

# Tính phân bố nhị thức Px,n biết số phép thử n và xác suất biến cố ngẫu nhiên trong mối phép thử p, và giá trị bằng x.

# Biến ngẫu nhiên x có thể nhận các giá trị nguyên 0, 1, 2 ...n. Xác suất để trong n phép thử biến cố xuất x lần được tính theo công thức Bernouille :

# Px,n = (nCx)*p^x * q^(n-x), trong đó q = 1 - p

# Tính tổ hợp chập x trong n phần tử được tính theo công thức : 


# Lưu ý chỉ lấy đến 6 số cuối của phần thập phân

# Input:

# Dòng đầu tiên số bộ test n (1 ≤N ≤ 10).

# N dòng tiếp theo, mỗi dòng gồm 3 số n, p, x với n là số phép thử và xác suất biến cố ngẫu nhiên trong mối phép thử p, và giá trị bằng x.

# Output

# In ra mỗi dòng giá trị của phân bố nhị thức.

 

# Input	

# 1
# 3 0.45 4

 
# Output
# 0.238367

