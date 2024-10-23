[m, n] = input().split()

a = list(map(int, input().split()))
my_dict = {}
for i in a:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1