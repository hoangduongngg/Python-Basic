def So_nho_con_thieu(a,n):
    for i in range(1,n+2):
        if a.count(i)==0:
            return i

n = int(input())
a = [int(x) for x in input().split()]
print (So_nho_con_thieu(a,n))