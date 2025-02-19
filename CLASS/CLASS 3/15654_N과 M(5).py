import sys
from itertools import permutations


def generate_sequences(arr, m):
    sequences = permutations(arr, m)
    for seq in sequences:
        print(*seq)


def sol():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    generate_sequences(arr, m)


sol()
