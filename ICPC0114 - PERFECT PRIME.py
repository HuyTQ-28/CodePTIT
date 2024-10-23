import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve(n):
    if not isPrime(int(n)) or not isPrime(int(n[::-1])):
        return "No"
    sum = 0
    for i in n:
        if i != '2' and i != '3' and i != '5' and i != '7':
            return "No"
        sum += int(i)
    if not isPrime(sum):
        return "No"
    return "Yes"


for t in range(int(input())):
    n = input()
    print(solve(n))