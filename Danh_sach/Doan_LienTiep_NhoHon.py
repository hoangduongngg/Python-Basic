def Run(n,a):
    
    return 0
t = int(input())
while t>0:
    n = int(input())
    a = input()
    Run(n,a)

    t-=1
# Idea: Dung Stack
# PY02050 ĐOẠN LIÊN TIẾP NHỎ HƠN

# Cho dãy số A[] có N phần tử. Với mỗi vị trí thứ i trong dãy, hãy tính độ dài của đoạn liên tiếp tính từ i trở về phía trước mà các giá trị đều nhỏ hơn hoặc bằng A[i].

# Input: Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.

# Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 105).
# Dòng tiếp theo gồm N số nguyên A1, A2, …, AN (1 ≤ A[i] ≤ 106).
# Output

# Với mỗi bộ test, in ra dãy kết quả trên một dòng.

# Input

# 1
# 7
# 100 80 60 70 60 75 85

# Output
# 1 1 1 2 1 4 6