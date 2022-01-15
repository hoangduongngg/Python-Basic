import re
def ThongKe(s):
    # covert to word
    ktdb = re.compile('\W') #\W: all ky tu trừ A->z ,0-9
    s = re.sub(ktdb, ' ', s.lower()) #thay ktdb = " "
    words = s.split() 

    # add dict to list 
    dif_words = []
    for word in set(words):
        dif_words.append({'word': word, 'count' : words.count(word) })

    # sort & print(res)
    res = sorted(dif_words, key = lambda k:(-k['count'], k['word']))
    for dic in res:
        print(dic.get('word'), dic.get('count'))

t = int(input())
s = ""
while t>0:
    s += input() +" "
    t-=1
ThongKe (s)

# Input

# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.

# PY03004 THỐNG KÊ TỪ KHÁC NHAU

# Bài làm tốt nhất
# Cho một đoạn văn bản có N dòng trong đó có thể có các dấu câu như dẩy phẩy (,) dấu chấm (.) dấu chấm hỏi (?) dấu chấm cảm (!) dấu hai chấm (:) dấu chấm phẩy (;) dấu ngoặc đơn, dấu gạch ngang (-), dấu gạch chéo (/).  

# Hãy liệt kê các từ khác nhau xuất hiện trong đoạn văn bản theo thứ tự số lần xuất hiện giảm dần.

# Chú ý:

# Khi thống kê thì không phân biệt chữ hoa, chữ thường.
# Bỏ qua các dấu câu đã liệt kê ở trên khi tách từ
# Input

# Dòng đầu ghi số N không quá 1000.

# Tiếp theo là N dòng mô tả văn bản. Mỗi dòng không quá 500 ký tự.

# Output

# Ghi ra danh sách các từ (ở dạng in thường) theo thứ tự số lần xuất hiện giảm dần.

# Trong trường hợp số lần xuất hiện bằng nhau thì liệt kê theo thứ tự từ điển tăng dần.

 

# Ví dụ


# Output

# ptit 4

# 2021 2

# dong 2

# ho 2

# nam 2

# sinh 2

# tro 2

# va 2

# vien 2

# 2019 1

# 2020 1

# 2022 1

# 500000 1

# 6 1

# benh 1

# dich 1

# dinh 1

# duy 1

# hien 1

# hoc 1

# hon 1

# khi 1

# khong 1

# muc 1

# on 1

# phi 1

# tang 1

# tri 1

# trich 1

# trong 1

# ty 1

# voi 1

# xuat 1