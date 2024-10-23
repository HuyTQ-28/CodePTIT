n = int(input())
a = [float(i) for i in input().split()]

Maxx, Minn = max(a), min(a)
lst = []
for i in a:
    if i != Maxx and i != Minn:
        lst.append(i)
print(f"{sum(lst) / len(lst):.2f}")