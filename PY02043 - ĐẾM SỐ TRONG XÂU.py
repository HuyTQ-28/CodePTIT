import re

for t in range(int(input())):
    s, n = input(), input()
    res = re.findall(n, s)
    print(len(res))