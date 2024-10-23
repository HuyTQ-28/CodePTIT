
s = input()
lower = 0
for character in s:
    if character.islower():
        lower += 1
if lower >= len(s) - lower:
    print(s.lower())
else:
    print(s.upper())