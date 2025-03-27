# n : 재료 개수
# g : 식용 불가 임계 세균 수의 합
# k : 버릴 수 있는 재료 개수의 상한값
# 각 재료의 [부패 속도 s, 유통 기한 l, 중요 여부 1 or 0 (1 = 뺄 수 있음) o]
# 세균 수 = s * max(1,x - l)
# 최대 k개의 재료를 버려서 세균 수의 합이 g 이하가 된다면 식용 가능
# 구매 일로 부터 며칠 까지 식용 가능 한가?

import sys

s_arr, l_arr, o_arr = [], [], []
n, g = 0, 0


def is_possible(day_after):
    total_g = 0
    for i in range(n):
        total_g += s_arr[i] * (max(1,(day_after - l_arr[i])))
    print(f'total : {total_g}')
    return total_g > g


def sol():
    read = sys.stdin.read().splitlines()
    global n, g
    n, g, k = map(int, read[0].split())

    global s_arr, l_arr, o_arr
    s_arr, l_arr, o_arr = [0] * n, [0] * n, [0] * n
    for i in range(n):
        s_arr[i], l_arr[i], o_arr[i] = map(int, read[i + 1].split())

    temp = [(0.0, 0)] * n
    for i in range(n):
        temp[i] = (l_arr[i] / s_arr[i], i)
    temp.sort()

    n = n - k
    for _, i in temp:
        if k == 0: continue
        if o_arr[i] == 0: continue
        s_arr = s_arr[:i] + s_arr[i + 1:]
        l_arr = l_arr[:i] + l_arr[i + 1:]
        k -= 1

    left = min(l_arr)
    right = 1 << 30
    answer = right
    while left <= right:
        mid = (left + right) // 2
        print(f'left : {left} || mid : {mid} || right : {right}')
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)


sol()

