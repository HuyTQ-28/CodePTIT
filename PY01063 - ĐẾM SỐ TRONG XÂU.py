
for t in range(int(input())):
    s = input()
    n = input()

    i, res = 0, 0
    while i <= len(s) - len(n):
        text = s[i:i+len(n)]
        if text == n:
            res += 1
            i += len(n)
        else:
            i += 1
    print(res)