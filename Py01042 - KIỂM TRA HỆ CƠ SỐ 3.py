def solve(s):
    for i in range(len(s)):
        if not (s[i] >= '0' and s[i] <= '2'):
            return 'NO'
    return 'YES'

for t in range(int(input())):
    s = input()
    print(solve(s))