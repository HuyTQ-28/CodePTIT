s = input()

while len(s) > 1:
    idx = len(s) // 2
    num1 = int(s[:idx])
    num2 = int(s[idx:])
    s = str(num1 + num2)
    print(s)