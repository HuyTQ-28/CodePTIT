
def check(s):
    sum, n = [0, len(s)]
    for i in range(1, n):
        x1, x2 = [int(s[i]), int(s[i - 1])]
        if abs(x1 - x2) != 2:
            return False
        sum += x2
    sum += int(s[n - 1])
    return sum % 10 == 0

for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")