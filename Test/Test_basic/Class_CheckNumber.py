import math
from Class_Prime import Prime

class CheckNumber(Prime):
    def __init__(self, n):
        super().__init__(n)
    
    def parity_check(self):
        if self.n%2:
            print(f"{self.n} is a odd number")
        else:
            print(f"{self.n} is a even number")
    
    def is_prime(self):
        super().isprime()
        
    def is_perfect(self):
        n = self.n
        sum = 0
        for i in range(1, (n//2)+1):
            if n%i==0:
                sum+=i
        if sum == n:
            print(f"{self.n} is a perfect number")
        else:
            print(f"{self.n} is not a perfect number")
    
    def is_square(self):
        temp = math.sqrt(self.n)
        if  temp == int(temp):
            print(f"{self.n} is a square number")
        else:
            print(f"{self.n} is not a square number")
        
n = CheckNumber(int(input()))
n.parity_check()
n.is_prime()
n.is_perfect()
n.is_square()