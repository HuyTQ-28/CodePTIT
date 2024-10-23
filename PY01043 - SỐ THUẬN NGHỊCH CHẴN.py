
def check(n):
    if len(n) % 2 != 0 or n != n[::-1]:
        return False
    for c in n:
        if int(c) % 2 != 0:
            return False
    return True

for t in range(int(input())):
    n = int(input())
    for i in range(22, n, 2):
        if check(str(i)):
            print(i, end=' ')
    print()