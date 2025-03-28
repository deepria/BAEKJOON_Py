# n : 재료 개수
# g : 식용 불가 임계 세균 수의 합
# k : 버릴 수 있는 재료 개수의 상한값
# 각 재료의 [부패 속도 s, 유통 기한 l, 중요 여부 1 or 0 (1 = 뺄 수 있음) o]
# 세균 수 = s * max(1,x - l)
# 최대 k개의 재료를 버려서 세균 수의 합이 g 이하가 된다면 식용 가능
# 구매 일로 부터 며칠 까지 식용 가능 한가?

import sys

s_arr, l_arr, o_arr = [], [], []
n, g, k = 0, 0, 0


def is_possible(day_after):
    bacteria = []
    for i in range(n):
        b = s_arr[i] * max(1, day_after - l_arr[i])
        bacteria.append((b, o_arr[i]))
    bacteria.sort(reverse=True)
    total = 0
    removed = 0
    for b, o in bacteria:
        if o == 1 and removed < k:
            removed += 1
            continue
        total += b
    return total <= g


def sol():
    read = sys.stdin.read().splitlines()
    global n, g, k
    n, g, k = map(int, read[0].split())

    global s_arr, l_arr, o_arr
    s_arr, l_arr, o_arr = [0] * n, [0] * n, [0] * n
    for i in range(n):
        s_arr[i], l_arr[i], o_arr[i] = map(int, read[i + 1].split())

    left = 1
    right = max(l_arr) + g + 1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


sol()
