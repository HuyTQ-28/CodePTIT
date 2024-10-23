def solve(n):
    count = 0
    for c in n:
        if c == '4' or c == '7':
            count += 1
    return (count == 4 or count == 7)

n = input()
print('YES' if solve(n) else 'NO')