def DiaChi_IP (s):
    a = s.split('.')
    if len(a)!=4: return 0
    for i in a:
        if not i.isnumeric():   return 0 #Kiem tra co phai so khong
        if int(i) <0 or int(i)>255: return 0
    return 1

def Check(s):
    if DiaChi_IP(s): print("YES")
    else: print("NO")

t = int(input())
while t>0:
    Check(input())
    t-=1

# Input:

# 2
# 192.168.1.1
# 256.255.255.255

# Output:

# YES
# NO