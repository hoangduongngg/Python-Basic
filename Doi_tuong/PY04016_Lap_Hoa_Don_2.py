from datetime import datetime

class KhachHang:
    def __init__(self, stt, Ten, Phong, NgayDen, NgayDi, PhatSinh ) -> None:
        self.Ma = "KH" + '%02d'%stt
        self.Ten = Ten.strip()
        self.Phong = Phong.strip()
        self.NgayDen = NgayDen.strip()
        self.NgayDi = NgayDi.strip()
        self.PhatSinh = int(PhatSinh)
        self.SoNgay = self.Xuly_SoNgay()
        self.ThanhTien = self.Xuly_ThanhTien()


    def Xuly_SoNgay (self):
        day_in = datetime.strptime(self.NgayDen, '%d/%m/%Y')
        day_out = datetime.strptime(self.NgayDi, '%d/%m/%Y')
        return (day_out - day_in).days +1

    def Xuly_ThanhTien(self):
        if self.Phong[0] == '1': Tien1Ngay = 25
        elif self.Phong[0] == '2': Tien1Ngay = 34
        elif self.Phong[0] == '3': Tien1Ngay = 50
        else: Tien1Ngay = 80

        return Tien1Ngay * self.SoNgay + self.PhatSinh

    def __str__(self) -> str:
        return '{} {} {} {} {}'.format(self.Ma, self.Ten, self.Phong, self.SoNgay, self.ThanhTien)
        

t = int(input())
stt=0
ds = []
while t>0:
    stt+=1
    ds.append(KhachHang(stt, input(),input(),input(),input(), input()))
    t-=1

for i in sorted(ds, key=lambda k: -k.ThanhTien):
    print(i)

# PY04016 LẬP HÓA ĐƠN - 2

# Khách sạn XYZ có đơn giá (theo ngày) được quy định khác nhau theo từng tầng. Khách hàng đến thuê phòng sẽ được tính tổng số tiền ở theo đơn giá cộng thêm chi phí dịch vụ phát sinh nếu có.

# Tầng - Giá
# 1 - 25
# 2 - 34
# 3 - 50
# 4 - 80

# Hãy giúp khách sạn tính tiền phải trả cho từng khách hàng và sắp xếp theo thứ tự tổng tiền giảm dần.

# Input

# Dòng đầu ghi số khách hàng (không quá 20)

# Mỗi khách hàng ghi trên 4 dòng gồm:

# Tên khách hàng (xâu ký tự độ dài không quá 100)
# Số phòng
# Ngày nhận phòng (định dạng dd/mm/yyyy)
# Ngày trả phòng (định dạng dd/mm/yyyy)
# Tiền dịch vụ phát sinh (số nguyên dương nhỏ hơn 100)
# Output

# Ghi ra danh sách đã được sắp xếp theo tổng tiền giảm dần bao gồm lần lượt các thông tin:

# Mã khách hàng (tự động tăng theo thứ tự nhập, tính từ KH01)
# Tên khách hàng
# Số phòng
# Số ngày ở
# Thành tiền
# Ví dụ
# Input


# 3
# Huynh Van Thanh   
# 103 
# 05/06/2010   
# 05/06/2010   
# 15
# Le Duc Cong  
# 106 
# 08/03/2010   
# 01/05/2010   
# 220
# Tran Thi Bich Tuyen   
# 207 
# 10/04/2010   
# 21/04/2010   
# 96

# Output
# KH02 Le Duc Cong 106 55 1595
# KH03 Tran Thi Bich Tuyen 207 12 504
# KH01 Huynh Van Thanh 103 1 40