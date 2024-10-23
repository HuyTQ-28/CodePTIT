# Sang so nguyen to
isPrime = [0] * (10**6 + 5)
isPrime[0] = isPrime[1] = 1
for i in range(2, 1001):
    if (isPrime[i] == 0):
        for j in range(i * i, 1000001, i):
            isPrime[j] = 1

# Quy hoach dong
dp = [0] * (10 **6 + 1)
for i in range(7, 1000001):
    if isPrime[i] == 0 and isPrime[i - 6] == 0 and (isPrime[i - 2] == 0 or isPrime[i - 4] == 0):
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

#TestCase
for t in range(int(input())):
    n = int(input())
    print(dp[n])