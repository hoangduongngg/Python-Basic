class SoPhuc:
    def __init__(self, a,b): 
        # a + bi 
        self.a = a
        self.b = b
    
    def Tong2So (self, o):
        return SoPhuc(self.a + o.a, self.b + o.b)

    def Tich2So (self, o):
        thuc = self.a* o.a - self.b*o.b
        ao = self.a*o.b + self.b*o.a
        return SoPhuc(thuc, ao)

    def __str__(self) -> str:
        return '{} + {}i'.format(self.a, self.b)

t = int(input())
while t>0:
    a = [int(i) for i in input().split()]
    A = SoPhuc(a[0], a[1])
    B = SoPhuc(a[2], a[3])
    TongAB = A.Tong2So(B)
    C = A.Tich2So(TongAB)
    D = TongAB.Tich2So(TongAB)
    print(f"{C}, {D}")
    t-=1

# A = a+bi, B = c+di 
# A*B = (ac - bd) + (ad+bc)i

# Input

# 3
# 1 2 3 4
# 2 3 4 5
# 1 -2 5 -6

# Output
# -8 + 14i, -20 + 48i
# -12 + 34i, -28 + 96i
# -10 - 20i, -28 - 96i