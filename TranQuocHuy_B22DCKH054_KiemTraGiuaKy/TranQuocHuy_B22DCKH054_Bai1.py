m, n = map(int, input().split())
matrix = []

for i in range(m):
    matrix.append(list(map(int, input().split())))

# b = [[0] * n for _ in range(m)]
# d = 0
#
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             if i == 0 or j == 0:
#                 b[i][j] = 1
#             else:
#                 b[i][j] = min(b[i - 1][j], b[i][j - 1], b[i - 1][j - 1]) + 1
#             d = max(b[i][j], d)
#
# print (f"Maximum area of square that only contains 1s: {d * d}")

d = 0
b = [[0] * n for _ in range(m)]

for i in range(n):
    b[0][i] = matrix[0][i]

for i in range(1, m):
    for j in range(n):
        if matrix[i][j] == 1:
            b[i][j] = b[i - 1][j] + 1

for i in range(m):
    st, l, r = [], [0] * n, [0] * n
    for j in range(n):
        while len(st) > 0 and b[i][st[-1]] >= b[i][j]:
            st.pop()
        if len(st) > 0:
            l[j] = st[-1]
        else:
            l[j] = -1
        st.append(j)
    st = []
    for j in range(n - 1, -1, -1):
        while len(st) > 0 and b[i][st[-1]] >= b[i][j]:
            st.pop()
        if len(st) > 0:
            r[j] = st[-1]
        else:
            r[j] = n
        st.append(j)
    for j in range(n):
        if matrix[i][j] == 1:
            d = max(b[i][j] * (r[j] - l[j] - 1), d)

print(f"Maximum area of rectangle that only contains 1s: {d}")