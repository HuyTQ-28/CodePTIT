def check(A, B):
    if len(A) != len(B):
        return "NO"
    for i in range(len(A)):
        if A[i] != B[i]:
            return "NO"
    return "YES"

[n, m] = input().split()
A = sorted(set(map(int, input().split())))
B = sorted(set(map(int, input().split())))

print(check(A, B))