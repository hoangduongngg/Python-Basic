import math
class Circle():
    def __init__(self, O, R):
        self.O = O
        self.R = R
    def describe(self):
        print(f"The Circle with center O{self.O} radios = {self.R}")
    
    def get_area(self):
        return math.pi*(self.R**2)
    def get_perimeter(self):
        return 2*math.pi*self.R

x = Circle((1,2),  3)
x.describe()
print (round(x.get_area(), 2), round(x.get_perimeter(), 2))