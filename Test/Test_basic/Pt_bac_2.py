import math
def Giai_pt_1(a,b):
    if a==0:
        if b==0:
            print ("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        print(-a/b)

def Giai_pt_2(a,b,c):
    if a==0:
        Giai_pt_1(b,c)
    else:
        delta = b**2-4*a*c
        if delta==0:
            print(f"Nghiem kep: {-b/(2*a)}")
        elif delta<0:
            print("Vo nghiem")
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print (x1, x2)

a,b,c = map(int, input().split())
Giai_pt_2(a,b,c)