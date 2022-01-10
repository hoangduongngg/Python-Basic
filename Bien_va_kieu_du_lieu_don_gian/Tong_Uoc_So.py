def Tong_Uoc_So (n):
    res = 0
    while n%2==0:
        res+=2
        n/=2
    i = 3
    while i<=n:
        while n%i==0:
            res+=i
            n/=i
        i+=2
    return res

t = int(input())
Tong_Uoc = 0
while t>0:
    Tong_Uoc += Tong_Uoc_So(int(input()))
    t-=1
print(Tong_Uoc)

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