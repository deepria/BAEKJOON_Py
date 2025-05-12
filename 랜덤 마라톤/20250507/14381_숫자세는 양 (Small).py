def main():
    from sys import stdin, stdout
    read = stdin.read().splitlines()
    t = int(read[0]) + 1
    for i in range(1, t):
        n = int(read[i])
        s = set()
        flag = False
        for j in range(1, 101):
            mul = n * j
            for string in str(mul):
                s.add(string)
            if len(s) == 10:
                flag = True
                stdout.write(f'Case #{i}: {mul}\n')
                break
        if not flag:
            stdout.write(f'Case #{i}: INSOMNIA\n')


if __name__ == "__main__":
    main()
