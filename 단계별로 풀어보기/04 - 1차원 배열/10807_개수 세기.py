def sol():
    n, *arr, v = map(int, open(0).read().split())
    cnt = [1 if arr[i] == v else 0 for i in range(n)]
    print(sum(cnt))

def sol_opt_gpt4o():
    _, *arr, v = map(int, open(0).read().split())  # `n` 생략
    print(arr.count(v))  # 리스트에서 `v`의 개수 세기


sol()
