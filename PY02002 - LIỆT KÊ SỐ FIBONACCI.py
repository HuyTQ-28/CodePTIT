F = [1] * 100

def prepare():
    for i in range(3, 93):
        F[i] = F[i - 1] + F[i - 2]

prepare()
for t in range(int(input())):
    left, right = map(int, input().split())
    for i in range(left, right + 1):
        print(F[i], end=" ")
    print()