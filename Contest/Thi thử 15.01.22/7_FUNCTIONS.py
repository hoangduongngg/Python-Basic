def Ktra_HopLe (s):
    if len(s) <6 or len(s) >12:
        return 0
    flag = 0
    for i in s:
        if i.islower():
            flag = 1
            break
    if flag == 0: return 0
    
    flag = 0
    for i in s:
        if i.isupper():
            flag = 1
            break
    if flag == 0: return 0
    
    flag = 0
    for i in s:
        if i.isnumeric():
            flag = 1
            break
    if flag == 0: return 0
   
    flag = 0
    for i in s:
        if '$'==i or '@'==i or '#'==i:
            flag = 1
            break
    if flag == 0: return 0
    
    return 1


def Ktra_MK (s):
    a = s.split(',')
    res = []
    for i in a:
        if Ktra_HopLe(i):
            res.append(i)
    print(','.join(res))
    

t = int (input())
while t>0:
    s = input()
    Ktra_MK (s)
    t-=1

# FUNCTIONS

 

# Một hệ thống phần mềm yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
# Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.

# Các tiêu chí kiểm tra mật khẩu bao gồm:

# 1. Ít nhất 1 chữ cái nằm trong [a-z]
# 2. Ít nhất 1 số nằm trong [0-9]
# 3. Ít nhất 1 kí tự nằm trong [A-Z]
# 4. Ít nhất 1 ký tự nằm trong [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12

# Viết chương trình kiểm tra tính hợp lệ của một chuỗi các mật khẩu xem chúng có đáp ứng những tiêu chí trên hay không và in ra những mật khẩu đúng tiêu chí.

# Input

# Dòng đầu ghi số bộ test, không quá 100.

# Mỗi bộ test chứa một chuỗi các mật khẩu phân tách nhau bởi dấu phẩy và không quá 10 mật khẩu.

# Output

# Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.

# Ví dụ:

# Input	

# 2
# ABd1234@1,a F1#,2w3E*,2We3345
# Ptit@123, PTIT2022

# Output
# ABd1234@1
# Ptit@123