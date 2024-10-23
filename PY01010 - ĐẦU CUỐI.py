def check(num):
    if (num[0] != num[-2]):
        return False
    if (num[1] != num[-1]):
        return False
    return True

for t in range(int(input())):
    num = input()
    if (check(num)):
        print("YES")
    else:
        print("NO")