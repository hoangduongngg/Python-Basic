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

    dic = {}
    res = 0
    for i in dic:
        res += i*dic.get(i)
    return res

def Xuly(a):
    res = 1
    for i in a:
        res *= Tong_thuaso(i)
    return res

t = int(input())
a = []
while t>0:
    n = int(input())
    a.append(n)
    t-=1

print(Xuly(a))

# 5 
# 7
# 9 
# 10 
# 13 
# 100

# KIỂU DỮ LIỆU ĐƠN GIẢN

# Cho N số nguyên. Nhiệm vụ của bạn là phân tích các số nguyên đã cho dưới dạng tích của các thừa số nguyên tố, sau đó bạn tính tổng các thừa số này và cuối cùng tính tích tổng trên.

# Input:

# Dòng đầu tiên số nguyên N (1 ≤≤ N ≤ 106).

# N dòng tiếp theo, mỗi dòng gồm một số nguyên có giá trị không vượt quá 2*106.

# Output

# In ra một số nguyên là đáp án tìm được.

# Ví dụ

# Input:	Output:
# 5 

# 7

# 9 

# 10 

# 13 

# 100

# 53508

# Giải thích test:

# 7 = 7

# 9 = 3 x 3 --> 3 + 3 = 6

# 10 = 2 x 5 --> 2 + 5 = 7

# 13 = 13

# 100 = 2 x 2 x 5 x 5 --> 2+2+5+5 = 14

# Nhân lại, 7 x 6 x 7 x 13 x 14 = 53508