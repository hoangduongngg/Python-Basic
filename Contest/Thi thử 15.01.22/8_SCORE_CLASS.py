from decimal import Decimal
class ThiSinh:
    def __init__(self, Ten, CC, BTL, CK) -> None:
        self.Ten = Ten
        self.CC = Decimal(CC)
        self.BTL = Decimal(BTL)
        self.CK = Decimal(CK)

    def TinhTB (self):
        return self.CC * Decimal(0.1) + self.BTL *Decimal(0.3) + self.CK * Decimal(0.6)
    def __str__(self) -> str:
        return self.Ten + " " + "%.1f"%self.TinhTB()

a = ThiSinh (input(), input(),input(),input())
print(a)

# Nguyen Van A
# 10
# 7
# 8