s = input()

n = 0
if len(s) % 2 != 0:
    n = len(s) - 1
else:
    n = len(s)

my_set = set()
for i in range(0, n - 1, 2):
    my_set.add(s[i] + s[i + 1])
res = sorted(list(my_set))
print(*res)