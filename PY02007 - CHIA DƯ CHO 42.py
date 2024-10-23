
cnt = 10
st = set()
while cnt != 0:
    a = [int(i) % 42 for i in input().split()]
    st.update(a)
    cnt -= len(a)

print(len(st))