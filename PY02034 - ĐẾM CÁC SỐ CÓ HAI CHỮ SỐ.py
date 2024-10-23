s = input()

n = 0
if len(s) % 2 != 0:
    n = len(s) - 1
else:
    n = len(s)

my_dict = {}
for i in range(0, n - 1, 2):
    num = s[i] + s[i + 1]
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

for x, y in my_dict.items():
    print(x, y)