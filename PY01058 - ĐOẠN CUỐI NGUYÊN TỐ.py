import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return n > 1


for t in range(int(input())):
    s = input()
    s = s[len(s) - 4:]
    if (isPrime(int(s))):
        print('YES')
    else:
        print('NO')