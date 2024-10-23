import math
for t in range(int(input())):
    n = input()
    rvn = n[::-1]
    if (math.gcd(int(n), int(rvn)) == 1):
        print("YES")
    else:
        print("NO")