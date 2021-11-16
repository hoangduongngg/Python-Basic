import math
def NhiPhan_Batphan(n):
    while len(n)%3!=0:
        n = '0'+ n
    lists = []
    for i in range(0, int (len(n)/3)):
        lists.append('')
        for j in range(i*3, i*3+3):
            lists[i]+= n[j]
    
    res= ''
    for num in lists:
        res += str(NhiPhan_ThapPhan(num))
    return res
    
def NhiPhan_ThapPhan(n):    #n:str
    k = 2 #he so = 10
    res = 0
    n = list(reversed(n))
    for i in range(0, len(n)):
        res += int(n[i]) * math.pow(k,i)
    return int(res)
    
    print(lists)

n = input()
print(NhiPhan_Batphan(n))