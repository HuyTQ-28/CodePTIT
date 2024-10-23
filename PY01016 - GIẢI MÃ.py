for t in range(int(input())):
    s = input()
    n = len(s)
    for i in range(0, n, 2):
        for cnt in range(int(s[i + 1])):
            print(s[i], end='')
    print()