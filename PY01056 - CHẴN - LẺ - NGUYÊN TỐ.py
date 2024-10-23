import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(s):
    n, summm = [len(s), 0]
    for i in range(n):
        summm += int(s[i])
        if (i % 2 == 0 and int(s[i]) % 2 != 0) or (i % 2 != 0 and int(s[i]) % 2 == 0):
            return False
    return isPrime(summm)

for t in range(int(input())):
    s = input()
    print('YES' if check(s) else 'NO')