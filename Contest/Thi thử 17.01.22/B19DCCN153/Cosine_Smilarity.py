import math
def Cos (a, b):
    n = len(a)
    tuso = A = B = 0
    for i in range(0,n):
        tuso += a[i]*b[i]
        A += a[i]**2
        B += b[i]**2

    mauso = math.sqrt(A) * math.sqrt(B)
    return tuso / mauso

def Xuly(a,ds):
    for i in ds:
        i['cos'] = Cos(a, i.get('chiso'))
    ds = sorted(ds, key=lambda k: -k['cos'])
    print(ds[0].get('name'), end=" [")
    for i in ds[:-1]:
        print('%.4f'%i.get('cos'), end = ", ")
    print('%.4f'%ds[-1].get('cos'), end = ']')

N = int(input()) #sodong
n = int(input()) #sochieu
a = [float(i) for i in input().split()]
ds = []
for i in range(0, N-3):
    s = input().split()
    x = [int(i) for i in s[1:]]
    ds.append({'name': s[0], 'chiso':x})

if N<4 or n>1024:
    print("INVALID INPUT")
else:
    Xuly(a, ds)

# 6
# 3
# 0.9 0.07 0.03
# Ngan 1 0 0
# Minh 0 1 0
# Nhung 0 0 1