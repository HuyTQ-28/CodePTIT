

for t in range(int(input())):
    n, d = [int(i) for i in input().split()]
    arr = list(map(int, input().split()))
    for i in range(n):
        print(arr[(i + d) % n], end=' ')
    print()