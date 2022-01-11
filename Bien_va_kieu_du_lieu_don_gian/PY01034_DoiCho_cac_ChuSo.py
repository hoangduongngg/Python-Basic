def DoiCho(s):
    s = [int(i) for i in list(s)]
    j = k = 0
    for i in range(len(s)-1, 0, -1):
        if s[i]<s[i-1]:
            j = i-1
            break
    if j==0: return "-1"
    Max = -1 #Gia tri lon nhat nho hon s[j]
    for i in range(j, len(s)):
        if Max < s[i] <s[j] :
            Max = s[i]
            k = i
    
    tmp = s[j]
    s[j]=s[k]
    s[k] = tmp

    return s

t = int (input())
while t>0:
    print(*DoiCho(input()),  sep= "")
    t-=1

# Idea: 
# B1: Tìm chữ số tăng đầu tiên từ trái qua phải, vị trí j
# B2: Từ j tìm max(các chữ số từ j đến cuối dãy and nhỏ hơn số tại j), ví trí k
# B3: Đổi chỗ
# PY01034 ĐỔI CHỖ CÁC CHỮ SỐ

# Cho một số nguyên không âm N được biểu diễn như một xâu ký tự. Hãy sử dụng nhiều nhất một phép đổi chỗ các chữ số trong N sao cho ta nhận được số lớn nhất nhỏ hơn N. Phép biến đổi có số 0 cho số đầu tiên sẽ không được chấp nhận. Ví dụ số N=354 thì số lớn nhất nhỏ hơn N được tạo ra là 345. Số 100 sẽ không có phép biến đổi vì số 010 có số 0 đứng đầu.
# Input:
# Dòng đầu tiên đưa vào số lượng test T (T≤100).
# Những dòng kế tiếp đưa vào các test. Mỗi bộ test là một xâu ký tự bao gồm các ký tự số. Độ dài tối đa là 1000.

# Output:
# Với mỗi test in ra số nguyên lớn nhất tìm được trên một dòng. Nếu không tồn tại đáp án, in ra -1.

# Input:

# 4
# 354
# 999
# 100
# 11101
 
# Output:
# 345
# -1
# -1
# 11011