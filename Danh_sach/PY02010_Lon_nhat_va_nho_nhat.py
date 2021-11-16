#PY02010
def Min_Max_String(a):
    if min(a)==max(a):
        print("BANG NHAU")
    else:
        print(f"{min(a)} {max(a)}")

while True:
    n = int(input())
    if n==0:
        break
    t = 0
    a = []
    while t<n:
        a.append(int(input()))
        t+=1
    Min_Max_String(a)

# def Min_Max_String(a):
#     a = [Xuly_0(x) for x in a]
#     a = sorted(a, key= lambda k:(len(k), str(k)))
#     if a[0]==a[-1]:
#         print("BANG NHAU")
#     else:
#         print(f"{a[0]} {a[-1]}")

# def Xuly_0(str):
#     res = ''
#     i = 0
#     while i <len(str):
#         if str[i]!='0':
#             res = str[i:]
#             break
#         i+=1
#     return res
# while True:
#     n = int(input())
#     if n==0:
#         break
#     t = 0
#     a = []
#     while t<n:
#         a.append(input())
#         t+=1
#     Min_Max_String(a)
