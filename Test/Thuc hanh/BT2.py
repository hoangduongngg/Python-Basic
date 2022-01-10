s = "restart"
char=s[0]
for i in s[1:]:
    s = s.replace(char, '$')
    s = char + s[1:]

print(s)