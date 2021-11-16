s1, s2 = input(), input()
p = int(input()) - 1 #do vi tri dau tinh la 1
res = s1[0:p] + s2 + s1[p:]
print(res)