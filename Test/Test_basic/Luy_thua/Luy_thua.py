def BT3(x,y):
    if x<0 or y<0:
        return 0
    res = 1
    for i in range(0,y):
        res*=x
    return res