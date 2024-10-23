def getPoint(n):
    result = 1.0
    if n >= 3 and n <= 4:
        result = 2.5
    elif n >= 5 and n <= 6:
        result = 3.0
    elif n >= 7 and n <= 9:
        result = 3.5
    elif n >= 10 and n <= 12:
        result = 4.0
    elif n >= 13 and n <= 15:
        result = 4.5
    elif n >= 16 and n <= 19:
        result = 5.0
    elif n >= 20 and n <= 22:
        result = 5.5
    elif n >= 23 and n <= 26:
        result = 6.0
    elif n >= 27 and n <= 29:
        result = 6.5
    elif n >= 30 and n <= 32:
        result = 7.0
    elif n >= 33 and n <= 34:
        result = 7.5
    elif n >= 35 and n <= 36:
        result = 8.0
    elif n >= 37 and n <= 38:
        result = 8.5
    elif n >= 39 and n <= 40:
        result = 9.0
    return result


def roundPoint(point):
    gap = point - int(point)
    if gap < 0.25:
        return int(point)
    elif gap <= 0.5 or gap < 0.75:
        return int(point) + 0.5
    return int(point) + 1

for t in range(int(input())):
    [rea, lis, spea, wri] = input().split()
    overall = (getPoint(int(rea)) + getPoint(int(lis)) + float(spea) + float(wri)) / 4
    print(f"{roundPoint(overall):.1f}")