def sol():
    read = input()
    str_arr = [c for c in read]
    arr = [-1 for _ in range(26)]
    for s in str_arr:
        arr[(ord(s) - 97)] = read.index(s)

    print(*arr, sep=' ')


sol()
