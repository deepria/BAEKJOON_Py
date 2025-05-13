def main():
    import sys
    read = sys.stdin.readline
    n, k = map(int, read().split())
    dolls = list(map(int, read().split()))
    left = 0
    lion_count = 0
    min_len = float('inf')
    for right in range(n):
        if dolls[right] == 1:
            lion_count += 1
        while lion_count >= k:
            min_len = min(min_len, right - left + 1)
            if dolls[left] == 1:
                lion_count -= 1
            left += 1
    print(min_len if min_len != float('inf') else -1)


if __name__ == "__main__":
    main()
