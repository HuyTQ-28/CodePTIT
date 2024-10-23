import math


def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n > 1

def solve(n):
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    print("YES" if isPrime(cnt) else "NO")

for t in range(int(input())):
    n = int(input())
    solve(n)