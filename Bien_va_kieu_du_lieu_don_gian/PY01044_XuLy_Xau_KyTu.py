def Giao_2Xau (s1, s2):
    s1 = sorted(set(s1.lower().split()))
    s2 = sorted(set(s2.lower().split()))

    res = []
    for i in s1:
        if i in s2: res.append(i)
    print(" ".join(res))

def Hop_2Xau (s1, s2):
    # s1 = s2 = ""
    res = sorted((s1 +" "+ s2).lower().split())
    res = sorted(set(res))
    print(" ".join(res))

s1 = input()
s2 = input()
Hop_2Xau(s1, s2)
Giao_2Xau(s1, s2)

# PY01044 XỬ LÝ XÂU KÝ TỰ

# Trong lập trình cơ bản, một từ được hiểu là một dãy ký tự liên tiếp không chứa khoảng trống, dấu tab hoặc dấu xuống dòng.

# Viết chương trình nhập hai dòng ký tự và hiển thị hợp và giao của hai tập từ tương ứng. Các từ trong tập từ không được phép trùng nhau, mỗi từ chỉ liệt kê một lần và theo đúng thứ tự từ điển. Các từ đều được chuyển hết về chữ viết thường. 

# Input

# Chỉ có 2 dòng, mỗi dòng có độ dài không quá 1000 ký tự.

# Output

# Dòng 1 ghi hợp của 2 tập từ theo thứ tự từ điển

# Dòng 2 ghi giao của 2 tập từ theo thứ tự từ điển.

# Ví dụ

# Input
# Lap  trinh  huong  doi  tuong
# Ngon  ngu  lap  trinh  C++

# Output

# c++ doi huong lap ngon ngu trinh tuong

# lap trinh