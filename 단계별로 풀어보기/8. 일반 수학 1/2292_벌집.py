def sol():
    n = int(input())
    i = 1
    s = n
    while s > 1:
        s = s - (6*i)
        i +=1
    print(1 if n == 1 else i)

sol()