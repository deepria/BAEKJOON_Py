def sol():
    x = int(input())
    n = 1
    while (n * (n + 1)) // 2 < x:
        n += 1

    start = (n * (n - 1)) // 2 + 1
    idx = x - start

    if n % 2 == 1:
        numerator = n - idx
        denominator = 1 + idx
    else:
        numerator = 1 + idx
        denominator = n - idx

    print(f"{numerator}/{denominator}")


sol()
