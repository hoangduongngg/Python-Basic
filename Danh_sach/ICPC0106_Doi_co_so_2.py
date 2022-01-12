import math
def Nhiphan_Doicoso (s,k):
    if k == 2: return s
    x = 2
    while 1:
        if pow(2, x) == k:
            break
        x+=1

    if len(s)%x!=0:
        s = (x-len(s)%x)*'0' + s
    a = [int(i) for i in list(s)]
    res = ""
    for i in range(0, len(a)+1-x,x):
        tmp = 0
        for j in range(0, x):
            tmp += a[i+j]*pow(2, x-1-j)
        if tmp<10: res += str(tmp)
        else: res+= chr(ord('A') + tmp-10)

    return res
    
t = int(input())
while t>0:
    k = int(input())
    n = input()
    print(Nhiphan_Doicoso (n,k))
    t-=1

# Idea: Tương tự cách lm NhiPhan - Bát phân : lấy 3 chữ số 1
# Cơ số 2: 1cs 1 lần (return this)
# Cơ số 4: 2cs 1 lần 
# Cơ số 16: 4cs 1 lần

# ICPC0106 ĐỔI CƠ SỐ - 2

# Cho xâu nhị phân X[] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

# Input:

# Dòng đầu tiên đưa vào T là số lượng bộ test.
# Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
# T, n, X[] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤10^5; X[i] =0, 1;
# Output:

# Đưa ra kết quả mỗi test theo từng dòng.

# Input:

# 2
# 8
# 10010100010010101
# 2
# 10010100010010101

# Output:

# 224225

# 10010100010010101

# def NhiPhan_BatPhan (s):
#     if len(s)%3!=0:
#         s = (3-len(s)%3)*'0' + s
#     a = [int(i) for i in list(s)]
#     res = ""
#     for i in range(0, len(a)-2,3):
#         res += str(a[i]*4 + a[i+1]*2 + a[i+2])
#     return res