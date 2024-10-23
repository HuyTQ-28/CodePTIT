words1 = input().lower().split()
words2 = input().lower().split()

intersection = set(words1).intersection(words2)
uni = set(words1).union(words2)

a1 = sorted(intersection)
a2 = sorted(uni)

print(*a2)
print(*a1)