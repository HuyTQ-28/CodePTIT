import math
for t in range(int(input())):
    N, X, M = [float(i) for i in input().split()]
    res = math.log(M/ N, 1 + X / 100)
    print(int(math.ceil(res)))