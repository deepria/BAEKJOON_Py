def main():
    from sys import stdin
    read = [*map(int, stdin.read().rstrip().split())]
    n, arr = read[0], read[1:]
    st = set()
    for a in range(n):
        if arr[a] != 0:
            st.add(arr[a])
            temp = str(arr[a])
            for b in range(a+1, n):
                temp = temp + str(arr[b])
                st.add(int(temp))
        else:
            st.add(arr[a])
    ss = sorted(st,reverse=True)
    for i in range(max(ss)):
        p = ss.pop()
        if i != p:
            print(i)
            break


if __name__ == "__main__":
    main()
