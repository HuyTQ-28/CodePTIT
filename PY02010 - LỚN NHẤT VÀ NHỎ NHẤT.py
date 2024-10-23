
while True:
    n = int(input())
    if n == 0:
        break

    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)
    arr.sort()
    if arr[0] == arr[len(arr) - 1]:
        print("BANG NHAU")
    else:
        print(arr[0], arr[len(arr) - 1])