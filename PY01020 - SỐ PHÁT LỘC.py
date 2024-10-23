
for t in range(int(input())):
    num = input()
    n = len(num)
    if (num[n - 1] == '6' and num[n - 2] == '8'):
        print("YES")
    else:
        print("NO")