
while True:
    Mylist = [int(i) for i in input().split()]
    if Mylist[0] == Mylist[1] == Mylist[2] == Mylist[3] == 0:
        break

    cnt = 0
    while True:
        if Mylist[0] == Mylist[1] == Mylist[2] == Mylist[3]:
            break
        tmp = Mylist.copy()
        for i in range(3):
            Mylist[i] = abs(tmp[i] - tmp[i + 1])
        Mylist[3] = abs(tmp[3] - tmp[0])
        cnt += 1
    print(cnt)