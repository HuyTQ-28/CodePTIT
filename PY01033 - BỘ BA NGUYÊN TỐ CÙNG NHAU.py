import math

l, r = [int(i) for i in input().split()]

for i in range(l, r - 1):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if math.gcd(i, k) == 1 and math.gcd(j, k) == 1 and math.gcd(i, j) == 1:
                print(f'({i}, {j}, {k})')