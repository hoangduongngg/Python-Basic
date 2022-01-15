import math
def Tong_thuaso (n):
    # if n==1: return 1
    dic = {}
    if n%2==0:
        dic[2] = 0
        while n%2==0:
            dic[2]+=1
            n = int(n/2)
    for i in range(3,int(math.sqrt(n))+1, 2):
        if n%i==0:
            dic[i] = 0
            while n%i==0:
                dic[i]+=1
                n = int(n/i)
    if n!=1: dic[n] =1

    res = 0
    for i in dic:
        res += i*dic.get(i)
    return res

def Xuly(a):
    res = 0
    for i in a:
        res += Tong_thuaso(i)
    return res

t = int(input())
a = []
while t>0:
    n = int(input())
    a.append(n)
    t-=1

print(Xuly(a))

# PY01074 TỔNG ƯỚC SỐ

# Cho N số nguyên. Nhiệm vụ của bạn là phân tích các số nguyên đã cho dưới dạng tích của các thừa số nguyên tố, sau đó tính tổng các ước số nguyên tố này.
# Input:
# Dòng đầu tiên số nguyên N (1 ≤≤ N ≤ 106).
# N dòng tiếp theo, mỗi dòng gồm một số nguyên có giá trị không vượt quá 2*106.
# Output
# In ra một số nguyên là đáp án tìm được.

# Input:
# 5 
# 7
# 9 
# 10 
# 13 
# 100

# Output:
# 47