def multiply(a, b):
    mod = 1000000007
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]

def matrix_pow(n):
    base = [[1, 1], [1, 0]]

    if n == 1:
        return base

    if n % 2 == 0:
        half = matrix_pow(n // 2)
        return multiply(half, half)
    else:
        half = matrix_pow((n - 1) // 2)
        return multiply(base, multiply(half, half))

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    for n in data:
        if n == -1:
            break
        elif n == 0:
            print(0)
        else:
            ans = matrix_pow(n)
            print(ans[0][1])

if __name__ == "__main__":
    main()