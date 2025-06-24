def convert_latex_symbols():
    replacements = {
        r"\\le": "<=",
        r"\\ge": ">=",
        r"\\dots": "...",
        r"\\cdots": "...",
        r"\\times": "×",
        r"\\div": "÷",
        r"\\neq": "!=",
        r"\\pm": "±",
        r"\\ ": " ",
        r"\$": ""
    }
    import re
    from sys import stdin, stdout
    text = stdin.read()
    for latex, symbol in replacements.items():
        text = re.sub(latex, symbol, text)

    text = re.sub(r'\.\s+', '.\n', text)

    # 줄 길이가 100자를 초과하는 경우에만 쉼표 뒤에 줄바꿈을 적용
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        if len(line) > 40:
            line = re.sub(r',\s+', ',\n', line)
        new_lines.append(line)
    text = '\n'.join(new_lines)

    # "예제 입력 N"과 "예제 출력 N" 뒤에 반드시 두 줄바꿈
    text = re.sub(r'(예제 입력 \d+)\n', r'\1\n\n', text)
    text = re.sub(r'(예제 출력 \d+)\n', r'\1\n\n', text)

    # 출력 숫자 줄 뒤에 반드시 두 줄바꿈
    text = re.sub(r'(예제 출력 \d+\n\n[^\n]+\n)(?=예제 입력|\Z)', r'\1\n', text)

    return text


if __name__ == "__main__":
    print(convert_latex_symbols())
