from decimal import Decimal


class ThiSinh:
    def __init__(self, stt, Ten, Diem, DanToc, KhuVuc) -> None:
        self.Ma = "TS" + '%02d'%stt
        self.Ten = Ten
        self.Diem = float(Diem)
        self.DanToc = DanToc
        self.KhuVuc = KhuVuc
        self.TongDiem = self.Xuly_TongDiem()
        self.TrangThai = self.Xuly_TrangThai()

    def ChuanHoaTen (self):
        res = ""
        a = self.Ten.strip().lower().split()
        for i in a:
            res += i.capitalize() + " "
        return res.strip()


    def Xuly_TongDiem(self):
        res = self.Diem
        if self.KhuVuc == '1': res += 1.5
        elif self.KhuVuc =='2': res += 1
        
        if self.DanToc != 'Kinh': res += 1.5
        return res

    def Xuly_TrangThai(self):
        if self.TongDiem >= 20.5: return "Do"
        return "Truot"

    def __str__(self) -> str:
        return self.Ma + " " + self.ChuanHoaTen() + " " + '%.1f'%self.TongDiem + " " + self.TrangThai

t = int(input())
ds = []
stt = 0
while t>0:
    stt+=1
    ds.append(ThiSinh(stt,input(),input(),input(),input()))
    t-=1

for i in sorted(ds, key= lambda k: (-k.TongDiem, k.Ma)):
    print(i)

# PYKT092 ĐIỂM TUYỂN SINH

# Bài làm tốt nhất
# Theo quy định mới, điểm tuyển sinh vào trường đại học XYZ sau khi tính tổng sẽ được cộng ưu tiên, cụ thể:

# Thí sinh khu vực 1 ưu tiên 1.5 điểm
# Thí sinh khu vực 2 ưu tiên 1 điểm
# Thí sinh khu vực 3 không ưu tiên
# Thí sinh dân tộc Kinh không ưu tiên
# Thí sinh các dân tộc khác ưu tiên 1.5 điểm
# Hãy tính tổng điểm đã ưu tiên và xác định tình trạng trúng tuyển. Biết điểm chuẩn của trường năm nay là 20.5 điểm.

# Input

# Dòng đầu ghi số thí sinh.

# Mỗi thí sinh ghi trên 4 dòng gồm:

# Họ tên: có thể chưa chuẩn hóa
# Điểm thi: giá trị số thực không quá 30
# Dân tộc
# Khu vực
# Output

# Ghi ra danh sách đã sắp xếp theo tổng điểm (đã tính ưu tiên) giảm dần, nếu tổng điểm bằng nhau thì sắp xếp theo mã thí sinh tăng dần. Các thông tin cần liệt kê gồm:

# Mã thí sinh (tính theo thứ tự nhập từ TS01)
# Họ tên đã chuẩn hóa
# Tổng điểm với đúng 1 chữ số phần thập phân
# Trạng thái: Do hoặc Truot
# Ví dụ
# Input

# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3

# Output

# TS01 Nguyen Hong Ngat 23.5 Do

# TS02 Chu Thi Minh 15.5 Truot

