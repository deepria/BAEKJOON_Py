def main():
    from sys import stdin
    read = stdin.read().splitlines()
    m = [*read[0].split()]
    fa, fb = read[1].split()
    a = ''.join([str(m.index(i)) for i in fa])
    b = ''.join([str(m.index(i)) for i in fb])
    ab = str(int(a) + int(b))
    fab = ''.join([str(m[int(i)]) for i in ab])
    print(fab)


if __name__ == "__main__":
    main()
