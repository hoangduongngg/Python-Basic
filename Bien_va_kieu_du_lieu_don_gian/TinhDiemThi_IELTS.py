import math
def DoiDiem (n):
    if n>=39: return 9.0
    if n>=37: return 8.5
    if n>=35: return 8.0
    if n>=33: return 7.5
    if n>=30: return 7.0
    if n>=27: return 6.5
    if n>=23: return 6.0
    if n>=20: return 5.5
    if n>=16: return 5.0
    if n>=13: return 4.5
    if n>=10: return 4.0
    if n>=7: return 3.5
    if n>=5: return 3.0
    if n>=3: return 2.5
    return 0


def TinhDiem (s):
    a = s.split()
    listen = DoiDiem(int(a[0]))
    speak = DoiDiem(int(a[1]))
    read = float(a[2])
    write = float(a[3])
    res = (listen + speak + read + write)/4
    res = float(6.6)
    # if res - int(res) == 0.25:
    #     return int(res) + 0.5
    # else:
    #     return round((res*2)/2)
    return round((res*2)/2)


t = int(input())
while t>0:
    print(TinhDiem (input()))
    t-=1

# Input:

# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0


# Output:

# 5.5

# 6.0