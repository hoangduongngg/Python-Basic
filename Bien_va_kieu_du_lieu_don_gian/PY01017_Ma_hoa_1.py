def Ma_hoa(s):
    lists = [s[0]]
    dem = [1]
    for i in range(1,len(s)):
        if s[i]==lists[-1]:
            dem[len(lists)-1]+=1
        else:
            lists.append(s[i])
            dem.append(1)

    for i in range(0, len(lists)):
        print(f"{dem[i]}{lists[i]}", end='')
    print()

t = int (input())
while t>0:
    s = input()
    Ma_hoa(s)
    t-=1