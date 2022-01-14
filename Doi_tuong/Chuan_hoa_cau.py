def ChuanHoaCau (s):
    s = s.lower()
    ktdb = ['.', '?', '!']
    

s = ""
while 1:
    try:
        s += input() + '\n'
    except:
        break