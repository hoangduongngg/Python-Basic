import re
def ThongKe(s,k):
    # covert to word
    ktdb = re.compile('\W') #\W: all ky tu A->z ,0-9
    s = re.sub(ktdb, ' ', s.lower()) #thay ktdb = " "
    words = s.split() 

    # add dict to list 
    dif_words = []
    for word in set(words):
        dif_words.append({'word': word, 'count' : words.count(word) })

    # sort & print(res)
    res = sorted(dif_words, key = lambda k:(-k['count'], k['word']))
    for dic in res:
        if dic.get('count') >=k:
            print(dic.get('word'), dic.get('count'))

t, k = map(int, input().split())
s = ""
while t>0:
    s += input() +" "
    t-=1
ThongKe (s,k)

# Input

# 3 2
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.

# Output
# ptit 4
# 2021 2
# dong 2
# ho 2
# nam 2
# sinh 2
# tro 2
# va 2
# vien 2
