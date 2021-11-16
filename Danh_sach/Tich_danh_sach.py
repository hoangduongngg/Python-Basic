def Tich(lists):
    res = 1
    for i in lists:
        res*=i
    return res

lists = [8,2,3,-1,7]
print(Tich(lists))