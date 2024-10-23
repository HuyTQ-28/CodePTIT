Prime = [1]*1005
Prime[0] = Prime[1] = 0
for i in range(2, 100):
    if Prime[i] == 1:
        for j in range(i*i, 1005, i):
            Prime[j] = 0

N, M = map(int, input().split())
arr = []
for i in range(N):
    tmp = [int(i) for i in input().split()]
    arr.append(tmp)

for i in range(N):
    for j in range(M):
        print(Prime[arr[i][j]], end=' ')
    print()