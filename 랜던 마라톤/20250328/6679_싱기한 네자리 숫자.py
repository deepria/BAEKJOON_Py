import sys

def to_base(n, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

def sol():
    for i in range(2992, 10000):
        i_12 = to_base(i, 12)
        i_16 = to_base(i, 16)
        sum_10 = sum(int(ch) for ch in str(i))
        sum_12 = sum(int(ch, 36) for ch in i_12)
        sum_16 = sum(int(ch, 36) for ch in i_16)
        if sum_10 == sum_12 == sum_16:
            sys.stdout.write(str(i) + '\n')
sol()