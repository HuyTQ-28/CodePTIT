N = 10**18
list = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            list += [i * j * k]
            k *= 5
        j *= 3
    i *= 2

list.sort()

def binSearch(left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == x:
            return mid + 1
        elif list[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return "Not in sequence"

for t in range(int(input())):
    n = int(input())
    print(binSearch(0, len(list), n))