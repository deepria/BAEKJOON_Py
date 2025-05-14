def fractal_block(level):
    if level == 1:
        return ['####', '#.#', '##', '#']
    prev = fractal_block(level - 1)
    expanded = []
    for idx, line in enumerate(prev, start=1):
        dots = '.' * (idx - 1)
        expanded.append(line + dots + line)
    return expanded + prev


file_path = "gen3.out"
try:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()
    block = fractal_block(9)
    block[506] = block[506][:450] + '####..##..##.######..##...##..##.....####...####..###..####...##..##'
    block[507] = block[507][:449] + '##..##.###.##...##...####..##.##.....##..##.##..##..##.##..##..#...#'
    block[508] = block[508][:449] + '##..##.##.###...##..##..##.####.........##..##..##..##.##..##..####'
    block[509] = block[509][:449] + '##..##.##..##...##..######.##.##......##....##..##..##.##..##..#.#'
    block[510] = block[510][:450] + '####..##..##...##..##..##.##..##....######..####...##..####...##'
    # print(len(lines))
    # print(len(block))

    for i in range(506, 511):
        print(block[i][440:])

    # for i in range(1024):
    #     if lines[i].strip() != block[i]:
    #         print(f'i:{i}')
    #         print(f'lines[i]: {lines[i]}')
    #         print(f'block[i]: {block[i]}')

    print('****************EOF****************')

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
