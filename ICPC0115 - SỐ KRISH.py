GT = [1]*10
for i in range(2, 10):
    GT[i] = GT[i - 1] * i

def solve(n):
    tmp = 0
    for i in n:
        tmp += GT[int(i)]
    if tmp == int(n):
        return "Yes"
    return "No"

for t in range(int(input())):
    n = input()
    print(solve(n))