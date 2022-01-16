def Rotate (s):
    res = ""
    xoay = 0
    for i in s:
        xoay += ord(i) - ord('A')
    for i in s:
        x = ord(i) - ord('A')   #giá trị của kí tự i
        res += chr(ord('A') + (x+xoay)%26) #26kytu
    return res

def MaHoa_DRM (s):
    s1 = Rotate(s[:len(s)//2])
    s2 = Rotate(s[len(s)//2:])

    #Merge
    res = ""
    for i in range(0, len(s1)):
        x = ord(s1[i]) - ord('A') #giá trị của ký tự i dãy s1
        y = ord(s2[i]) - ord('A') #giá trị của ký tự tương ứng bên dãy s2 - xoay
        res += chr(ord('A') + (x+y)%26)
    return res

t = int(input())
while t>0:
    print(MaHoa_DRM(input()))
    t-=1

# PY01040 MÃ HÓA 3

# Bài làm tốt nhất
# Cho một xâu ký tự. Quá trình mã hóa D - R - M sẽ trải qua ba bước Chia (Divide), Xoay (Rotate) và Trộn (Merge). Ví dụ với xâu: EWPGAJRB  quá trình này sẽ diễn ra như sau:

# Devide: Xâu ban đầu được chia thành 2 nửa: “EWPG” và “AJRB”.
# Rotate: Với mỗi nửa, tính toán giá trị xoay của nó bằng cách tính tổng giá trị các ký tự. (A = 0; B = 1; … Z = 25).  Giá trị xoay của “EWPG” là 4 + 22 + 15 + 6 = 47. Tiến hành xoay xâu  “EWPG”  đi 47 ký tự (tính cả bước chuyển từ Z về A nếu cần) ta sẽ được xâu: “ZRKB”. Tương tự, “AJRB” được chuyển thành “BKSC”
# Merge: Trong bước này, mỗi ký tự trong xâu thứ nhất sẽ được xoay theo giá trị của ký tự ở vị trí tương ứng trong xâu thứ 2. Trong ví dụ trên, chữ Z trong xâu thứ nhất sẽ xoay theo giá trị B, tức là 1 vị trí. Do đó sẽ chuyển thành chữ A. Tiếp tục thực hiện với các ký tự tiếp theo ta sẽ có kết quả là “ABCD”.
# Cho một xâu ký tự chỉ bao gồm các chữ cái in hoa với số lượng ký tự là chẵn, bạn hãy tìm xâu mã hóa DRM tương ứng.

# Input

# Dòng đầu ghi số bộ test T (T≤30).

# Mỗi bộ test ghi trên một dòng xâu ký tự cần mã hóa, chỉ gồm các chữ cái in hoa, độ dài là chẵn và không quá 15000 ký tự.

 

# Output

# Với mỗi test in ra trên một dòng kết quả mã hóa DRM tương ứng.


# Input

# 3
# EWPGAJRB
# BB
# TPQJDRJWSQXGRRIPXFMINTELHBJA

# Output

# ABCD

# E

# FIRSTDATAFILEV