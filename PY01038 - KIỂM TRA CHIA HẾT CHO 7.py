def process(n):
    cnt = 0
    while cnt <= 1000:
        if n % 7 == 0:
            return n

        cnt += 1
        rvn = str(n)
        rvn = rvn[::-1]
        n += int(rvn)
    return -1



for t in range(int(input())):
    n = input()
    print(process(int(n)))