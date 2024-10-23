

for t in range(int(input())):
    n = int(input())
    dd = [0] * 1005
    while n > 0:
        dd[int(input())] += 1
        n -= 1

    key, value = [-1, 0]
    for i in range(1000, 0, -1):
        if dd[i] >= value:
            key = i
            value = dd[i]
    print(key)