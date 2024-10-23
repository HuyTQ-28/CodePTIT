import math

n = int(input())
res, row, col =  [0, [0]*n, [0]*n]
for i in range(n):
    txt = input()
    for j in range(len(txt)):
        if txt[j] == 'C':
            row[i] += 1
            col[j] += 1

for i in row:
    if i >= 2:
        res += math.comb(i, 2)
for i in col:
    if i >= 2:
        res += math.comb(i, 2)
print(res)