import math

F = [0] * 2000005

def TongUoc(n):
    res = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n /= i
                res += i
    if n > 1:
        res += n
    return res

for n in range(2, 2000001):
    F[n] = TongUoc(n)

ans = 0
for n in range(int(input())):
    ans += F[int(input())]
print(int(ans))
