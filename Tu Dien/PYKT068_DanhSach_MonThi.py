class MonHoc:
    def __init__(self, MaMH, TenMH, HinhThucThi):
        self.MaMH = MaMH
        self.TenMH = TenMH
        self.HinhThucThi = HinhThucThi

    def toString(self):
        return f"{self.MaMH} {self.TenMH} {self.HinhThucThi}"

t = int(input())
dsmh = []
while t>0:
    dsmh.append(MonHoc (input(), input(), input()))
    t-=1

res = sorted (dsmh, key = lambda k: k.MaMH)
print(res)
for i in res:
    print(i.toString())

# Input

# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen


# Output

# BAS1203 Giai tich 1 Thi viet + Van dap truc tuyen
# MUL1320 Nhap mon da phuong tien Bai tap lon + Van dap truc tuyen

