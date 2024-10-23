import math

def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n > 1

n, a = int(input()), list(map(int, input().split()))
for i in range(n - 1):
    if isPrime(a[i]):
        for j in range(i + 1, n):
            if isPrime(a[j]) and a[j] < a[i]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
print(*a)