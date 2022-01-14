from decimal import Decimal
class ThiSinh:
    def __init__(self, TenSV, DOB, Diem1, Diem2, Diem3):
        self.TenSV = TenSV
        self.DOB = DOB
        self.Diem1 = Decimal(Diem1)
        self.Diem2 = Decimal(Diem2)
        self.Diem3 = Decimal(Diem3)
        self.TongDiem = self.Tinh_Tong_Diem()
    
    def Tinh_Tong_Diem (self):
        return self.Diem1 + self.Diem2 + self.Diem3
    
    def toString(self):
        return "{} {} ".format(self.TenSV, self.DOB) + "{0:.1f}".format(self.TongDiem)

ts = ThiSinh (input(), input(),input(),input(),input())
print(ts.toString())

# Input

# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5

# Output
# Nguyen Hoang Ha 11/10/2001 20.0