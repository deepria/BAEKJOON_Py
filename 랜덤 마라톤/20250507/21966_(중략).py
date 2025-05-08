def main():
    from sys import stdin, stdout
    read = lambda: stdin.readline().strip()
    n = int(read())
    s = read()
    if n <= 25:
        print(s)
    else:
        temp = s[11:-11]
        t = temp.find('.')
        if t == len(temp) - 1 or t == -1:
            print(s[:11] + '...' + s[-11:])
        else:
            print(s[:9] + '......' + s[-10:])


if __name__ == "__main__":
    main()
