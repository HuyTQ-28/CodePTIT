

for t in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    freq = {}
    for x in a:
        if freq.get(x) is None: freq[x] = 1
        else: freq[x] += 1
    for x in freq:
        if freq[x] % 2 != 0:
            print(x)
            break