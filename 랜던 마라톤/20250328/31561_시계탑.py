def sol():
    m = int(input())
    if m <= 30:
        m /= 2
    else:
        m -= 30
        m = (m * 3) / 2 + 15

    print(round(m, 1))


sol()
