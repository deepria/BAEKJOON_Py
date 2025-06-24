def get_ops_best(a, b, k):
    if a > b:
        a, b = b, a
    def calc_ops(t):
        return (t - a) // k + (t - a) % k + (t - b) // k + (t - b) % k
    m = (b - a + k - 1) // k
    t1 = a + m * k
    t2 = b
    return min(calc_ops(t1), calc_ops(t2))


def main():
    from sys import stdin
    read = stdin.readlines()
    n, k = map(int, read[0].split())
    arr = list(map(int, read[1].split()))
    cnt = 0
    for i in range(n // 2):
        a, b = arr[i], arr[n - i - 1]
        if a != b:
            cnt += get_ops_best(a, b, k)
    print(cnt)


if __name__ == "__main__":
    main()

'''

5 7
5 16 32 14 28

7

2 10
2 11

2
'''
