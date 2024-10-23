def CountFrequency(Mylist):
    freq = {}
    for item in Mylist:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    res, cnt = Mylist[0], 1
    for key, value in freq.items():
        if value > cnt:
            res = key
            cnt = value
    print(res if 2 * cnt > len(Mylist) else "NO")

for t in range(int(input())):
    n = int(input())
    Mylist = [int(i) for i in input().split()]
    CountFrequency(Mylist)