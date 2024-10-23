# import re
#
# s = ''
# while True:
#     try:
#         s += input()
#     except EOFError:
#         break
#
# regex = '[\w\s,:]+'
# s = re.findall(regex, s)
# for i in s:
#     x = i.lower().split()
#     x[0] = x[0].title()
#     print(*x)

text = []
while True:
    try:
        text += input().lower().split()
    except EOFError:
        break

s = ''
for i in text:
    if i[-1] in '.?!':
        tmp = i.split('.')
        tmp = tmp[0].split('?')
        tmp = tmp[0].split('!')
        s += tmp[0]