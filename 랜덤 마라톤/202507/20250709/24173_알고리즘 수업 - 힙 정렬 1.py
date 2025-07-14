import sys

sys.setrecursionlimit(10 ** 6)
swap_count, answer = 0, tuple()


def heap_sort(a, n, k):
    global swap_count, answer
    answer = None
    for i in range(n // 2, 0, -1):
        heapify(a, i, n, k)
    for i in range(n, 1, -1):
        record_swap(a, 1, i, k)
        if answer:
            return
        heapify(a, 1, i - 1, k)


def heapify(a, k, n, k_th):
    left = 2 * k
    right = 2 * k + 1
    if right <= n:
        if a[left] < a[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    if a[smaller] < a[k]:
        record_swap(a, k, smaller, k_th)
        if answer:
            return
        heapify(a, smaller, n, k_th)


def record_swap(a, i, j, k_th):
    global swap_count, answer
    swap_count += 1
    if swap_count == k_th:
        x, y = a[i], a[j]
        answer = (min(x, y), max(x, y))
    a[i], a[j] = a[j], a[i]


if __name__ == "__main__":
    read = sys.stdin.readline
    n, k = map(int, read().split())
    tmp = list(map(int, read().split()))
    a = [None] + tmp
    heap_sort(a, n, k)
    if answer:
        print(answer[0], answer[1])
    else:
        print(-1)
