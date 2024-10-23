
n = int(input())
matrix = [[]] * n
for i in range(n):
    matrix[i] = [int(x) for x in input().split()]
k = int(input())

up, down = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            up += matrix[i][j]
        elif i > j:
            down += matrix[i][j]

sub = abs(up - down)
print('YES' if sub <= k else 'NO')
print(sub)