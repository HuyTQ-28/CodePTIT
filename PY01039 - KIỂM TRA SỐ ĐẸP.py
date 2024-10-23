def solve(n):
    for i in range(2, len(n)):
        if n[i] != n[i - 2]:
            return 'NO'
    return 'YES'

for t in range(int(input())):
    n = input()
    print(solve(n))