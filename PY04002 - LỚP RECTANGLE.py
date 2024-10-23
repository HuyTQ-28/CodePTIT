class Rectangle:
    def __init__(self, a, b, c) -> None:
        self.perimeter = (a + b) * 2
        self.area = a * b
        self.color = c[:1].upper() + c[1:].lower()



if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))