# def Tan_suat_le(a,n):
#     for i in list(set(a)):
#         if a.count(i)%2==1:
#             print(i)

def Tan_suat_le(a,n):
    a.sort()
    dem=1
    for i in range(0, n-1):
        if a[i]==a[i+1]:
            dem+=1
        else:
            if dem%2==1:
                return a[i]
            else:
                dem=1
    return a[-1]

t = int (input())
while t>0:
    n = int (input())
    a = [int(i) for i in input().split()]
    print(Tan_suat_le(a,n))
    t-=1