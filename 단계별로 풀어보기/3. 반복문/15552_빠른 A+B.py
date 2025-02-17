# import sys
# n = int(sys.stdin.readline().rstrip())  # 입력 개수
# for _ in range(n):
#     print(sum(map(int, sys.stdin.readline().rstrip().split())))

import sys


def sol():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = [str(arr[i] + arr[i + 1]) for i in range(0, n * 2, 2)]
    print('\n'.join(result) + '\n')


sol()
