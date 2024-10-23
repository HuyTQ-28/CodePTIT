
def solve(list, n):
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if list[i] > list[j]:
                res += 1
    print(res)

n = int(input())
list = [int(i) for i in input().split()]
solve(list, n)