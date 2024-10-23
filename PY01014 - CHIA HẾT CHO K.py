import math

a, K, N = [int(i) for i in input().split()]

x, check = 1, False
while K * x <= N:
    num = K * x - a
    if num > 0:
        print(num, end = ' ')
        check = True
    x += 1

if check == False:
    print('-1')