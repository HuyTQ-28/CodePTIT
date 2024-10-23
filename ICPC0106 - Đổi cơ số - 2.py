
def transformFour(n):
    while len(n) % 2 != 0:
        n = '0' + n

    res = ''
    for i in range(len(n) - 1, 0, -2):
        tmp = int(n[i]) + int(n[i - 1]) * 2
        res = str(tmp) + res
    print(res)

def transformEight(n):
    while len(n) % 3 != 0:
        n = '0' + n

    res = ''
    for i in range(len(n) - 1, 0, -3):
        tmp = int(n[i]) + int(n[i - 1]) * 2 + int(n[i - 2]) * 4
        res = str(tmp) + res
    print(res)

def transformHexa(n):
    X = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while len(n) % 4 != 0:
        n = '0' + n

    res = ''
    for i in range(len(n) - 1, 0, -4):
        tmp = int(n[i]) + int(n[i - 1]) * 2 + int(n[i - 2]) * 4 + int(n[i - 3]) * 8
        res = X[tmp] + res
    print(res)

for t in range(int(input())):
    b = int(input())
    n = input()
    if b == 2:
        print(n)
    elif b == 4:
        transformFour(n)
    elif b == 8:
        transformEight(n)
    else:
        transformHexa(n)