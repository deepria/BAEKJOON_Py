def sol():
    n, x, *arr = map(int, open(0).read().split())
    result = ''
    for i in range(n):
        if arr[i] < x:
            result += str(arr[i]) + ' '
    print(result)


sol()
