def solve(s):
    if len(s) < 3:
        return 'NO'
    arr = list(int(i) for i in s)
    up = True
    for i in range(1, len(arr)):
        if up and arr[i] <= arr[i - 1]:
            up = False
        elif not up and arr[i] >= arr[i - 1]:
            return 'NO'
    return 'YES'

for t in range(int(input())):
    n = input()
    print(solve(n))