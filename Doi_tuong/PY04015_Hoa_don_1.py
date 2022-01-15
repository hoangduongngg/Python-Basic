class HoaDon():
    def __init__(self,stt,ten,cu,moi):
        self.MaKH = "KH" +"{0:02d}".format(stt)        
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.hientai = self.tinh()
        self.ThanhTien = self.tong()
    def tinh(self):
        return self.moi - self.cu
    def tong(self):
        if 0<= self.hientai <= 50:
            res = self.hientai*100
            res = res+ res*0.02
        elif 51<= self.hientai <= 100:
            res = 50*100 + (self.hientai-50)*150
            res = res+res*0.03
        else:
            res = 50*100 + 50*150 + (self.hientai-100)*200
            res = res+res*0.05

        return res
    def __str__(self):
        return '{} {} '.format(self.MaKH,self.ten) + '{0:.0f}'.format(self.ThanhTien)


t = int(input())
ds = []
for i in range(0, t):
    ds.append(HoaDon(i+1,input(),int(input()),int(input())))

for i in sorted(ds, key=lambda k:-k.ThanhTien):
    print(i)

# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612