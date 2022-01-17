def Xuly_Diem(s):
    for i in s:
        if i == '.':
            return s
    return s[0] + '.' + s[1:]

class NhanVien:
    def __init__(self, Ten, DiemLT, DiemTH ) -> None:
        self.Ten = Ten
        self.DiemLT = DiemLT
        self.DiemTH = DiemTH
        self.DiemTB = self.Xuly_DiemTB()
        self.XepLoai = self.Xep_Loai()

    def Xuly_DiemLT (self):
        return float(Xuly_Diem(self.DiemLT))

    def Xuly_DiemTH (self):
        return float(Xuly_Diem(self.DiemTH))
    
    def Xuly_DiemTB (self):
       return ( self.Xuly_DiemLT() + self.Xuly_DiemTH())/2

    def Xep_Loai(self):
        if self.Xuly_DiemTB() >9.5:
            return "XUAT SAC"
        if self.Xuly_DiemTB() >=8:
            return "DAT"
        if self.Xuly_DiemTB() >=5:
            return "CAN NHAC"
        return "TRUOT"
        

    def __str__(self) -> str:
        return self.Ten + " " + '%.2f'%self.DiemTB + " " + self.XepLoai


t = int(input())
ds = []
while t>0:
    ds.append(NhanVien(input(), input(), input()))
    t-=1
for i in sorted(ds, key = lambda k : (-k.DiemTB, k.Ten)):
    print(i)
# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56