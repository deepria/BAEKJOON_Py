from sys import stdin
from math import gcd
from functools import reduce


def lcm_two(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm_two, numbers)


def main():
    read = [*map(int, stdin.read().rstrip().split())]
    n, arr = read[0], read[1:]
    print(lcm_multiple(arr))


main()
