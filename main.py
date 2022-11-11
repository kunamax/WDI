from random import randint


def Factors(a):
    b = 2
    fac1 = 0
    fac2 = 0
    while b < a:
        if a % b == 0 and fac1 == 0:
            fac1 = b
            a /= b
            b -= 1
        elif a % b == 0 and fac2 == 0:
            fac2 = b
            a /= b
            b -= 1
        elif a % b == 0:

            return False
        b += 1
    return True


def Square(l):
    n = len(l)
    for i in range(2, n + 1):
        for x in range(0, n + 1 - i):
            for y in range(0, n + 1 - i):
                if Factors(l[x][y] * l[x + i - 1][y] * l[x][y + i - 1] * l[x + i - 1][y + i - 1]):
                    return i
    return 0


if __name__ == '__main__':
    size = 4
    list = [[randint(1, 20) for _ in range(size)] for _ in range(size)]
    #list = [[17, 1, 13, 16], [7, 3, 20, 2], [5, 10, 1, 13], [10, 7, 3, 16]]
    for i in list:
        print(i)
    print(Square(list))