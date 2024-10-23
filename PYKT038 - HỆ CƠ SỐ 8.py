s = input()
while len(s) % 3 != 0:
    s = '0' + s

res = ""
for i in range(len(s) - 1, 1, -3):
    num = int(s[i]) + int(s[i - 1]) * 2 + int(s[i - 2]) * 4
    res = str(num) + res
print(res)