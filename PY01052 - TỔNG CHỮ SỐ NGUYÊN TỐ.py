import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if (isPrime(sum)):
        print('YES')
    else:
        print('NO')