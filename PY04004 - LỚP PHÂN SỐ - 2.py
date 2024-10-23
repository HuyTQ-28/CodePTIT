import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def reduce(self):
        gcd = math.gcd(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd
        return self

    def add(self, o):
        res = PhanSo(self.tu * o.mau + o.tu * self.mau, self.mau * o.mau)
        return res.reduce()

s = input().split()
A = PhanSo(int(s[0]), int(s[1]))
B = PhanSo(int(s[2]), int(s[3]))
C = A.add(B)

print(f'{C.tu}/{C.mau}')
