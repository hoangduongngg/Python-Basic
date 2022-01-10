str = "HelloPython3#"
chu_thuong, chu_hoa, so, khac = 0
for s in str:
    if (s.islower()):
        chu_thuong+=1
    elif (s.isupper()):
        chu_hoa+=1
    elif (s.isnumeric()):
        so +=1
    else:
        khac+=1
print (chu_thuong, chu_hoa, khac)