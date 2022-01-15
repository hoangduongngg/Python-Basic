def SwapCase (s):
    res = ""
    for i in s:
        if 'a'<=i<'z': res += i.upper()
        else: res += i.lower()
    return res

s = input()
print(SwapCase(s))