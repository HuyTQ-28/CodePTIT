import math
def solve(n, k):
    left, right = [10**(k - 1), 10**k - 1]
    cnt = 0
    #print(left, right)
    for i in range(left, right + 1):
        if math.gcd(n, i) == 1:
            print(i, end=' ')
            cnt += 1
            if cnt % 10 == 0:
                print()

N, K = [int(i) for i in input().split()]
solve(N, K)