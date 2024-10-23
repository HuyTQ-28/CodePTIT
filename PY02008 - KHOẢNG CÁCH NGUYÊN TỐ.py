import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

Mylist = [0, 2]
def prepare():
    k = 3
    while len(Mylist) <= 1001:
        if isPrime(k):
            Mylist.append(k)
        k += 2

prepare()
N, X = [int(i) for i in input().split()]
for i in range(N + 1):
    X += Mylist[i]
    print(X, end=" ")