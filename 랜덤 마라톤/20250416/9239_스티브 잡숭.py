def find_numbers(x):
    result = []
    max_n = 10 ** 8

    p = int(x * 10000)
    q = 10000

    for k in range(1, 9):
        for d in range(1, 10):
            num = d * (q - p * (10 ** (k - 1)))
            denom = p - 10 * q

            if denom == 0 or num % denom != 0:
                continue

            r = num // denom
            if r < 0 or r >= 10 ** (k - 1):
                continue

            n = d * 10 ** (k - 1) + r
            if n >= max_n:
                continue

            m = r * 10 + d
            if abs(n * x - m) < 1e-6:
                result.append(n)

    return sorted(result)


def main():
    x = float(input())
    numbers = find_numbers(x)
    if not numbers:
        print("No solution")
    else:
        for n in numbers:
            print(n)


if __name__ == "__main__":
    main()
