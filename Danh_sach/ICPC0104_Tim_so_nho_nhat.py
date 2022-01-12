def Timso_NhoNhat (s):
    a = []
    i = 0
    while i<len(s):
        if '0'<= s[i] <= '9':
            tmp = ''
            while '0'<= s[i] <= '9':
                tmp += s[i]
                i+=1
                if i==len(s): break
            a.append(int(tmp))
        i+=1
    print(min(a))

t =int(input())
while t>0:
    Timso_NhoNhat(input())
    t-=1

# ICPC0104 TÌM SỐ NHỎ NHẤT

# Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.

# Input:

# Dòng đầu tiên đưa vào T là số lượng bộ test.
# Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
# T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
# Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
# Output:

# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:

# Input:


# 2
# 12ab29cd19
# ab123gh456cd
# Output:

# 12
# 123