import math

class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        tmp = math.gcd(self.x, self.y)
        self.x = int(self.x / tmp)
        self.y = int(self.y / tmp)

    def __str__(self):
        return f'{self.x}/{self.y}'

s = input().split()
p = PhanSo(int(s[0]), int(s[1]))
print(p)