# def Init(a, n, k):
#     i = k
#     while i >= 1 and a[i] == n - k + i:
#         i -= 1
#     if i < 0:
#         ok = False
#         return
#
#
# [n, k] = input().split()
# my_set = set(int(i) for i in input().split())
#
# a = list(my_set.copy())

a = [0]*100
def change_values():
    a[0] = 1
    a[1] = 2
change_values()
print(a)

