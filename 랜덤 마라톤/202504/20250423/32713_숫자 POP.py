from sys import stdin


def main():
    read = [*map(int, stdin.read().rstrip().split())]
    n, k, arr = read[0], read[1], read[2:]
    arr_set = {*arr}
    max_cnt = 0
    l = len(arr)
    for s in arr_set:
        index = arr.index(s)
        while True:
            cnt = 0
            temp_k = k
            for i in range(index, l):
                if s == arr[i]:
                    cnt += 1
                elif s != arr[i] and temp_k != 0:
                    temp_k -= 1
                else:
                    temp_k = k
                    cnt = 0

                if cnt > max_cnt:
                    max_cnt = cnt
            try:
                index += arr[index + 1:].index(s)
                index += 1
            except ValueError:
                break

    print(max_cnt)


main()


def main_debug():
    read = [*map(int, stdin.read().rstrip().split())]
    n, k, arr = read[0], read[1], read[2:]
    arr_set = {*arr}
    max_cnt = 0
    l = len(arr)
    for s in arr_set:
        print(arr)
        print(f's :{s}')
        index = arr.index(s)
        while True:
            print(f'index : {index}')
            cnt = 0
            temp_k = k
            for i in range(index, l):
                print(f'i :{arr[i]}')
                if s == arr[i]:
                    cnt += 1
                    print(f'cnt : {cnt}')
                elif s != arr[i] and temp_k != 0:
                    temp_k -= 1
                    print(f'temp_k : {temp_k}')
                else:
                    temp_k = k
                    cnt = 0

                if cnt > max_cnt:
                    max_cnt = cnt
                    print(f'max_cnt : {max_cnt}')
            try:
                index += arr[index + 1:].index(s)
                index += 1
            except ValueError:
                break

    print(max_cnt)


# main_debug()

'''
11 3
1 1 2 1 2 2 1 2 2 1 2

6

11 4
1 2 2 3 4 1 1 1 2 2 2

4

5 3
1 2 1 2 1

3
'''


def func(k, a):
    max_length = 0
    positions = {} # 숫자별 등장 위치 저장
    for idx, val in enumerate(a):
        if val not in positions:
            positions[val] = []
        positions[val].append(idx)

    # 각 숫자별로 가능한 연속 구간의 최대 길이 계산
    for val, pos_list in positions.items():
        left = 0
        for right in range(len(pos_list)):
            # 중간에 삭제해야 할 숫자 수가 K를 초과하면 왼쪽 이동
            while pos_list[right] - pos_list[left] - (right - left) > k:
                left += 1
            max_length = max(max_length, right - left + 1)

    return max_length

def sol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(func(k,a))

# sol()