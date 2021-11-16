def TCS(n,tcs):
    for i in n:
        tcs+=int(i)
    return str(tcs)

n = input()
count = 0
while len(n)>1:
    if n[0]=='-':
        tcs = ord('-')-ord('0')
        n = n[1:]
    else:
        tcs = 0
    
    n = TCS(n,tcs)
    count+=1
print(count)