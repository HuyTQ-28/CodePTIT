def solve(a, b):
    n = len(a)
    for i in range(1, n):
        if abs(ord(a[i]) - ord(a[i - 1])) != abs(ord(b[i]) - ord(b[i - 1])):
            return 'NO'
    return 'YES'

for t in range(int(input())):
    a = input()
    print(solve(a, a[::-1]))