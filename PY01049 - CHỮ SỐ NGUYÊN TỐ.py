import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(s):
    n, cnt = [len(s), 0]
    if (isPrime(n) == False):
        return False
    for i in s:
        if isPrime(int(i)):
            cnt += 1
    return cnt > n - cnt

for t in range(int(input())):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')