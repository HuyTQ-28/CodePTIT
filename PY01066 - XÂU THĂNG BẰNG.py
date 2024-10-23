def check(s):
    n = len(s)
    for i in range(n - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[n - i - 1]) - ord(s[n - i - 2])):
            return 'NO'
    return 'YES'


for t in range(int(input())):
    s = input()
    print(check(s))
