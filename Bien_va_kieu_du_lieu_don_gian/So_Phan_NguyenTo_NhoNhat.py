import math
MAX = pow(10,4)

def PhanTich_ThuaSo (n):
    res = {2:0}
    if n%2==0:
        while n%2==0:
            res[2] = res.get(2) + 1
            n/=2
    i = 3
    while i<=n:
        if n%i==0:
            res[i] = 0
            while n%i==0:
                res[i] = res.get(i) +1
                n/=i
        i+=2
    return res


def So_Uoc_So( Dict): 
    res = 1
    for i in Dict.keys():
        res *= (Dict.get(i) + 1)

    return res

def Day_Phan_NguyenTo():
    res = {}    #List luu cac so Phan Nguyen To
    UocSo_max = 0
    for i in range(1, MAX):
        if So_Uoc_So(PhanTich_ThuaSo(i)) > UocSo_max:
            UocSo_max = So_Uoc_So(PhanTich_ThuaSo(i))
            res[i] = 1
        else:
            res[i] = 0
    return res

# print(Day_Phan_NguyenTo())
t = int(input())
while t>0:
    n = int(input())
    while Day_Phan_NguyenTo().get(n) ==0:
        n+=1
    print(n)


    t-=1


# PY01037 SỐ PHẢN NGUYÊN TỐ NHỎ NHẤT
# Số nguyên dương N được gọi là phản nguyên tố nếu như số lượng ước số của N lớn hơn số lượng ước số của tất cả các số nguyên dương nhỏ hơn N.
# Ví dụ các số phản nguyên tố đầu tiên: 1, 2, 4, 6, 12, 24, …
# Cho số nguyên dương X, hãy tìm số phản nguyên tố bé nhất không nhỏ hơn X.

# Input:
# Dòng đầu ghi số bộ test T (không quá 10^6)
# Mỗi test ghi số nguyên dương X (1 ≤ X ≤ 10^7)
# Output:
# Với mỗi test, ghi ra kết quả tính được trên một dòng.
# Input
# 1
# 5
# Output
# 6

# => Ý tưởng: Lưu 1 list các số phản nguyên tố:
# Để tìm số ước của một số cho trước, ta chỉ việc phân tích ước của một số. 
# Sau đó lấy số mũ của các thừa số nguyên tố đó cộng với 1 rồi nhân với nhau.

# Ví dụ: 135 = 3^3 * 5
# => Số ước = (3+1)(1+1) = 8

