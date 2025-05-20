if __name__ == "__main__":
    import lzma

    data = open('gen4.out', 'rb').read()
    lzma_data = lzma.compress(data)
    print(f'origin data length:{len(data)}')
    print(f'lzma data length:{len(lzma_data)}')
    print(f'rate : {len(lzma_data)/len(data) *100}')

    # rest = lzma.decompress(enc)
    # print(data == rest)
