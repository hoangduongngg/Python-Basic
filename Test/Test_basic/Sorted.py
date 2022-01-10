a = ['523', '98', '111111']
#sort theo chu cai dau tien
print(sorted(a))
#sort so lon string:multi key
a = sorted(a, key= lambda k:(len(k), str(k))) 
print(a)