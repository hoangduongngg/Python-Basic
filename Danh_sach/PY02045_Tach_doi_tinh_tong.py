def Tachdoi_tinhtong(n):
    return str(int(n[:len(n)//2]) + int(n[len(n)//2:]))

n = input()
while len(n)>1:
    n = Tachdoi_tinhtong(n)
    print(n)