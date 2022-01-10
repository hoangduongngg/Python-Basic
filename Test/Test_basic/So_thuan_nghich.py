def So_thuan_nghich(n): #n:str
    if len(n)<2:
        return 0
    for i in range(len(n)//2):
        if n[i]!=n[-1-i]:
            return 0
    return 1


n = input()
if So_thuan_nghich(n):
    print("YES")
else:
    print("NO")