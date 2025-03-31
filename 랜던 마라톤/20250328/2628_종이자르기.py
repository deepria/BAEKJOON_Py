import sys


def get_max_gap(arr):
    return max(arr[i] - arr[i - 1] for i in range(1, len(arr)))


def sol():
    read = sys.stdin.read().splitlines()
    w, h = map(int, read[0].split())
    n = int(read[1])

    w_arr, h_arr = [0, w], [0, h]
    for i in range(2, n + 2):
        cmd, idx = map(int, read[i].split())
        if cmd == 1:
            w_arr.append(idx)
        else:
            h_arr.append(idx)
    w_arr.sort()
    h_arr.sort()
    print(get_max_gap(w_arr) * get_max_gap(h_arr))


sol()
