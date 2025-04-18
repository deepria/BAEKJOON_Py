cnt = 0
kth_swap = ()
kth_array_state = []


def heapify(arr, k, n):
    global cnt, kth_swap, kth_array_state
    left = 2 * k
    right = 2 * k + 1

    if right <= n:
        smaller = left if arr[left] < arr[right] else right
    elif left <= n:
        smaller = left
    else:
        return

    if arr[smaller] < arr[k]:
        arr[k], arr[smaller] = arr[smaller], arr[k]
        cnt += 1
        if cnt == target_k:
            kth_swap = (arr[k], arr[smaller])
            kth_array_state = arr[1:].copy()
        heapify(arr, smaller, n)


def build_min_heap(arr, n):
    for i in range(n // 2, 0, -1):
        heapify(arr, i, n)


def heap_sort(arr, n):
    global cnt, kth_swap, kth_array_state
    n = len(arr) - 1
    build_min_heap(arr, n)

    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        cnt += 1
        if cnt == target_k:
            kth_swap = (arr[1], arr[i])
            kth_array_state = arr[1:].copy()
        heapify(arr, 1, i - 1)


def sol():
    global target_k
    n, target_k = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    heap_sort(arr, n)

    if cnt < target_k:
        print(-1)
    else:
        print(*kth_array_state)


sol()
