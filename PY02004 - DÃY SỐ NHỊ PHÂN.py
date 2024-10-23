def solve(list, n):
    res = 0
    for i in range(0, n - 1):
        if list[i] != list[i + 1]:
            res += 1
    print(res)

n = int(input())
list = [int(i) for i in input().split()]
solve(list, n)