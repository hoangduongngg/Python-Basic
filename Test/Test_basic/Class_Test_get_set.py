from re import X
from tkinter import Y


class Poin:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __getattr__(self, name):
        print(name)
    def __setattr__(self, __name: int, __value: int):
        return 0
        
p = Poin(1,2)
print(p.x)