n = int(input())
arr = [int(i) for i in input().split()]

total_steps, idx_value = 10**9, 0
for i in range(n):
    tmp = arr[i]
    sum = 0
    for x in arr:
        sum += abs(x - tmp)
    if (sum < total_steps) or (sum == total_steps and idx_value > i):
        total_steps = sum
        idx_value = i
print(total_steps, arr[idx_value])