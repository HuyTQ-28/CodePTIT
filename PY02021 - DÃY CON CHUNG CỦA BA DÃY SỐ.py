def commonElements(A, B):
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            res.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return res

for t in range(int(input())):
    [n, m, k] = input().split()
    A = [int(i) for i in input().split()]
    B = [int(j) for j in input().split()]
    C = [int(k) for k in input().split()]
    # list tmp luu cac phan tu chung cua A va B
    tmp = commonElements(A, B)
    # list res luu cac phan tu chung cua A, B va C
    res = commonElements(tmp, C)
    if len(res) == 0:
        print("NO")
    else:
        print(*res)

