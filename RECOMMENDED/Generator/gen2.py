file_path = "gen2.out"
try:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readline()
    arr = lines.split(', ')

    arr2 = [1, 1]
    for i in range(2, 10000):
        temp = arr2[i - 2] + arr2[i - 1]
        if temp > 9099099909999099999:
            temp -= 9099099909999099999
        arr2.append(temp)
    arr2 = [str(i) for i in arr2]
    arr2.append('0.\n')
    print(*arr2,sep=', ')

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
