def main():
    numbers = [*map(int, input().split())]
    x = 1
    while True:
        count = sum(1 for num in numbers if x % num == 0)
        if count >= 3:
            print(x)
            break
        x += 1


if __name__ == "__main__":
    main()
