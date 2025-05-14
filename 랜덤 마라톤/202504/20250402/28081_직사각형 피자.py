def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def sol():
    from sys import stdin

    w, h, k = map(int, stdin.readline().split())
    _ = stdin.readline()
    y_a = [0] + list(map(int, stdin.readline().split())) + [h]
    _ = stdin.readline()
    x_a = [0] + list(map(int, stdin.readline().split())) + [w]

    dy_list = [y_a[i] - y_a[i - 1] for i in range(1, len(y_a))]
    dx_list = [x_a[i] - x_a[i - 1] for i in range(1, len(x_a))]

    dy_list.sort()
    dx_list.sort()

    cnt = 0
    for dx in dx_list:
        if dx == 0: continue
        threshold = k // dx
        idx = binary_search(dy_list, threshold)
        cnt += idx
    print(cnt)


sol()
