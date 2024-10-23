import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    s = input()
    pre, post = [s[0:3], s[len(s) - 3:]]
    if isPrime(int(pre)) and isPrime(int(post)):
        print("YES")
    else:
        print("NO")