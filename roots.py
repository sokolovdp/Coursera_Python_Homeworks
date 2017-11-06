import sys


def sqr_roots(a: "int", b: "int", c: "int"):
    d = ((b ** 2 - 4 * a * c) ** 0.5) / (2.0 * a)
    t = -b / (2.0 * a)
    x1 = int(t - d)
    x2 = int(t + d)
    print(x1)
    print(x2)


if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    sqr_roots(a, b, c)
