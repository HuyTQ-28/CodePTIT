

for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        sum = 0
        for i in range(2, n + 1, 2):
            sum += 1 / float(i)
        print(f"{sum:.6f}")
    else:
        sum = 0
        for i in range(1, n + 1, 2):
            #print(i, end=' ')
            sum += 1 / float(i)
        print(f"{sum:.6f}")