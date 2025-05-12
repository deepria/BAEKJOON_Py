def generate_recursive_block(size: int) -> list[str]:
    """
    Generates a recursive ASCII pyramid block of given size.
    Size must be a power of 2 (e.g. 4, 8, 16, ...).
    """
    if size < 1:
        return []

    lines = []

    # 1. 상단 4줄 고정 패턴
    lines.append("#" * size)  # 전부 #
    lines.append(("#." * (size // 2))[:size])  # 교차형
    lines.append(("##" + ".." * ((size - 2) // 2))[:size])  # 연속형
    lines.append(("#" + "..." * ((size - 1) // 3))[:size])  # 바깥만 #

    if size > 4:
        lines += generate_recursive_block(size // 2)

    return lines


def generate_pyramid_auto(h):
    return "\n".join(generate_recursive_block(h))


# 예시 실행
if __name__ == "__main__":
    print(generate_pyramid_auto(16))