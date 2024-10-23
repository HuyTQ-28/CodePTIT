
for t in range(int(input())):
    s = sum(int(i) for i in input())
    print('YES' if s % 3 == 0 else 'NO')