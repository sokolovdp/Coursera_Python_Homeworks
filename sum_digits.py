import sys


def sum_digits_in_string(line: "str") -> "int":
    return sum(int(c) for c in line)


if __name__ == '__main__':
    digit_string = sys.argv[1]
    print(sum_digits_in_string(digit_string))
