from datetime import datetime

class TramDoLuongMua:
    def __init__(self, stt, Ten, Time_Start, Time_End, LuongMua) -> None:
        self.Ma = 'T' + '%02d'%stt
        self.Ten = Ten
        self.Time_Start = datetime.strptime(Time_Start, '%H:%M')
        self.Time_End = datetime.strptime(Time_End, '%H:%M')
        self.LuongMua = LuongMua
        self.LuongMua_TB = self.Xuly_LuongMuaTB()

    def get_Ten (self):
        return self.Ten
        

    def ThoiGianMua (self):
        a = [int(i) for i in str(self.Time_End-self.Time_Start).split(':')]
        return a[0] + a[1]/60

    def Xuly_LuongMuaTB(self):

        return self.LuongMua / self.ThoiGianMua()

    def __str__(self) -> str:
        return '{} {} '.format(self.Ma, self.Ten) + '{0:.2f}'.format(self.LuongMua_TB)
    
t = int(input())
ds = []
stt=0
while t>0:
    stt+=1
    TenTram = input()
    Time_Start = input()
    Time_End = input()
    LuongMua = int(input())
    flag = 0
    for i in ds:
        if TenTram == i.get_Ten():
            flag == 1
            break
    
    if flag == 0:
        ds.append(TramDoLuongMua(stt, TenTram,Time_Start,Time_End,LuongMua))
    t-=1

for i in ds:
    print(i)

    

# PY04013 TÍNH TOÁN LƯỢNG MƯA

# Trong một ngày mưa nhiều, các trạm đo mưa hoạt động hết công suất. Tại mỗi trạm đo, các cơn mưa được ghi nhận thời điểm bắt đầu, thời điểm kết thúc và lượng mưa đo được. Một trạm mưa có thể có nhiều lần mưa trong ngày.

# Hãy tính lượng mưa trung bình trong 1 giờ (60 phút) của từng trạm theo đúng thứ tự trong danh sách ban đầu. Chú ý để tính lượng mưa trung bình thì cần tính tất các lần đo mưa tại trạm đó.

# Input

# Dòng đầu ghi số lượt đo lượng mưa.

# Thông tin về một lần đo lượng mưa gồm 4 dòng:

# Tên trạm
# Thời điểm bắt đầu mưa (hh:mm)
# Thời điểm kết thúc mưa (hh:mm)
# Lượng mưa đo được
# Số trạm đo khác nhau nhỏ hơn 10.

# Output

# Ghi ra danh sách các trạm khác nhau trong danh sách đo mưa và lượng mưa trung bình của từng trạm.

# Thông tin trên mỗi dòng lần lượt gồm:

# Mã trạm đo (tính từ T01). Chú ý: nếu cùng tên trong danh sách đo thì cũng sẽ cùng mà trạm.
# Tên trạm đo mưa
# Lượng mưa trung bình trong 1 giờ tại mỗi trạm (tính chính xác đến 2 số phần thập phân).
# Các thông tin ghi cách nhau một khoảng trống.

# Ví dụ

# Input


# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35

# Output

# T01 Dong Anh 59.22
# T02 Cau Giay 80.70
# T03 Soc Son 57.60