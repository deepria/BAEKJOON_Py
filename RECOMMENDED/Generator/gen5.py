if __name__ == "__main__":
    import lzma

    data = open('gen5.out', 'rb').read().splitlines()
    print(len(data))
    d = dict()
    for da in data:
        d[da] += 1
    print(d)

    # rest = lzma.decompress(enc)
    # print(data == rest)
