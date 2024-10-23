
n = int(input())
matrix = [[]] * n
for i in range(n):
    matrix[i] = [int(x) for x in input().split()]
k = int(input())

up, down = 0, 0
for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            up += matrix[i][j]
        elif j > n - i - 1:
            down += matrix[i][j]

sub = abs(up - down)
print('YES' if sub <= k else 'NO')
print(sub)