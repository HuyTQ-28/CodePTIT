
def solve(arr, n):
    fMin = 10 ** 9
    sMin = 10 ** 9
    tMin = 10 ** 9

    for i in range(n):
        if arr[i] < fMin:
            tMin = sMin
            sMin = fMin
            fMin = arr[i]
        elif arr[i] < sMin:
            tMin = sMin
            sMin = arr[i]
        elif arr[i] < tMin:
            tMin = arr[i]
    return fMin + sMin + tMin


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))