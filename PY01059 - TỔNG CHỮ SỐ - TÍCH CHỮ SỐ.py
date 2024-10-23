
def solve(s):
    cnt, tong, tich = [0, 0, 1]
    for i in range(len(s)):
        if i % 2 == 0:
            tong += int(s[i])
        else:
            if s[i] != '0':
                tich *= int(s[i])
                cnt += 1
    print(tong, end=' ')
    print(0 if tich == 1 and cnt == 0 else tich)

for t in range(int(input())):
    s = input()
    solve(s)