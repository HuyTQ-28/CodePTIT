Prime = [1] * 1000005

def seive():
    Prime[0] = Prime[1] = 0
    for i in range(2, 1001):
        if Prime[i] == 1:
            for j in range(i * i, 1000001, i):
                Prime[j] = 0

seive()
n = int(input())
a = [int(i) for i in input().split()]
res = {}
for i in a:
    if Prime[i] == 1:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1

for key, value in res.items():
    print(key, value)