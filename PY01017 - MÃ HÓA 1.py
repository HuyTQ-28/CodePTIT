def solve(s):
    n = len(s)
    i = 0
    while i < n:
        character = s[i]
        frequent = 1
        i += 1
        while i < n and character == s[i]:
            i += 1
            frequent += 1
        print(str(frequent) + character, end='')
    print()


for t in range(int(input())):
    s = input()
    solve(s)