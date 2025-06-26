def main():
    n = int(input())
    count = 0
    for a in range(1, n // 3 + 1):
        for b in range(a, (n - a) // 2 + 1):
            c = n - a - b
            if a + b > c:
                count += 1
    print(count)


if __name__ == "__main__":
    main()


# 정수 삼각형 공식 풀이
# def main() -> None:
#     n = int(input())
#     ans = (n * n + 6 * n * (n % 2) + 24) // 48
#     print(ans)
#

