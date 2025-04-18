from itertools import permutations
from collections import Counter


def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    total = 0
    prev = 0
    for c in reversed(s):
        val = roman[c]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total


def int_to_roman(num):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    return tens[num // 10] + ones[num % 10]


s = input().strip()
min_val = float('inf')
seen = set()

for p in permutations(s):
    r = ''.join(p)
    if r in seen:
        continue
    seen.add(r)
    try:
        val = roman_to_int(r)
        if 1 <= val < 100:
            roman_back = int_to_roman(val)
            if Counter(roman_back) == Counter(s):
                min_val = min(min_val, val)
    except:
        pass

print(int_to_roman(min_val))
