def check(n):
    for c in n:
        if c != '4' and c != '7':
            return False
    return True

for t in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")