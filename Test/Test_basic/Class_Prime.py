import math

class Prime():
    def __init__(self, n):
        self.n = n

    def SNT(self, x):
        if x==2:
            return 1
        if x%2 ==0 or x<2:
            return 0
        for i in range(3,int(math.sqrt(x))+1,2):
            if x%i == 0:
                return 0
        return 1

    def isprime(self):
        if self.SNT(self.n):
            print(f"{self.n} is a prime number")
        else:
            print(f"{self.n} is not a prime number")

    def next_prime(self):
        t = self.n + 1
        while self.SNT(t)!=1:
            t+=1
        return t
    
# n = Prime(int(input()))
# n.isprime()
# print(n.next_prime())