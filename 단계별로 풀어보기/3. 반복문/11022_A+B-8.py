import sys


def sol():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    result = [f'Case #{i // 2 + 1}: {arr[i]} + {arr[i + 1]} = ' + str(arr[i] + arr[i + 1]) for i in range(0, n * 2, 2)]
    print('\n'.join(result) + '\n')


sol()
