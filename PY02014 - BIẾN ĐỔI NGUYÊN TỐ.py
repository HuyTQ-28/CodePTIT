import math

#Seive of Eratosthenes
N = 11000
Prime = [1] * N
Prime[0] = Prime[1] = 0
for i in range(2, int(math.sqrt(N))):
    if Prime[i] == 1:
        for j in range(i * i, N, i):
            Prime[j] = 0
#Push all prime number into a list
Pr = []
for i in range(N):
    if Prime[i] == 1:
        Pr.append(i)
#Solve
n, a = int(input()), list(map(int, input().split()))
res = 0
for i in a:
    m = Pr[-1]
    for j in Pr: m = min(m, abs(i - j))
    res = max(res, m)
print(res)