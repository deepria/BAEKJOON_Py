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

    return text


if __name__ == "__main__":
    print(convert_latex_symbols())
