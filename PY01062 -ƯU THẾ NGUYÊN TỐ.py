import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(s):
    if isPrime(len(s)) == False:
        return False
    cnt = 0
    for i in s:
        num = int(i)
        if isPrime(num):
            cnt += 1
    return cnt > len(s) - cnt

for t in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")