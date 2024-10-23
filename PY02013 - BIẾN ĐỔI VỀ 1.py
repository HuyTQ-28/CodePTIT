
def solve(n):
    cnt = 1
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    print(cnt)

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)