def solve(s):
    res = 10 ** 19

    i = int(0)
    while i < len(s):
        if s[i].isdigit():
            tmp = int(s[i])
            i += 1

            while i < len(s) and s[i].isdigit():
                tmp = tmp * 10 + int(s[i])
                i += 1

            if tmp < res:
                res = tmp
        i += 1
    print(res)

for t in range(int(input())):
    s = input()
    solve(s)