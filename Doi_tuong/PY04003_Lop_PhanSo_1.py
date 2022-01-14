from math import gcd
class PhanSo:
    def __init__(self,tu, mau) -> None:
        self.tu = tu
        self.mau = mau
    def ToiGian (self):
        tu = self.tu//gcd(self.tu, self.mau)
        mau = self.mau//gcd(self.tu, self.mau)
        return "{}/{}".format(tu, mau)

if __name__ == "__main__":
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    print(p.ToiGian())