def So_loc_phat_dep(n):
    if n[0]=='8':
        return 0
    for i in range(0, len(n)-2):
        if n[i]!='6' and n[i]!='8':
            return 0
        if n[i] == n[i+1] == n[i+2] == '8':
            return 0
    return 1

n = input()
if So_loc_phat_dep(n):
    print("YES")
else:
    print("NO")