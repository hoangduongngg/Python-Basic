def Bien_doi(n):
    a = [n]
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        a.append(n)
    return len(a)

while 1:
    n = int(input())
    if n==0:
        break
    print(Bien_doi(n))