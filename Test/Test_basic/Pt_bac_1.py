def Giai_pt_1(a,b):
    if a==0:
        if b==0:
            print ("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        print(-a/b)

a,b = map(int, input().split())
Giai_pt_1(a,b)