import os


def sol_opt():
    tokens = map(int, iter(os.read(0, os.stat(0).st_size).split()))  # 바이너리 입력 처리
    next(tokens)  # 첫 번째 값(n)은 사용하지 않으므로 건너뜀
    a = 1 << 29  # 매우 큰 수 (약 536870912)
    b = -a  # 매우 작은 수 (약 -536870912)

    for x in tokens:  # 이터레이터 기반 반복
        if x < a:
            a = x
        if x > b:
            b = x

    os.write(1, (str(a) + ' ' + str(b)).encode())  # 바이너리 출력
    os._exit(0)  # 강제 종료 (빠름)


def sol():
    n, *arr = map(int, open(0).read().split())
    min_val = 1000000
    max_val = -1000000
    for i in range(n):
        temp = arr[i]
        if temp < min_val:
            min_val = temp
        if temp > max_val:
            max_val = temp
    print(f'{min_val} {max_val}')


sol()
