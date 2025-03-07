import sys


def get_gpa(grade):
    match grade:
        case "A+":
            return 4.5
        case "A0":
            return 4.0
        case "B+":
            return 3.5
        case "B0":
            return 3.0
        case "C+":
            return 2.5
        case "C0":
            return 2.0
        case "D+":
            return 1.5
        case "D0":
            return 1.0
        case "F":
            return 0.0
        case "P":
            return -1


def sol():
    sum_score = 0.0
    sum_grade = 0.0
    for _ in range(20):
        read = sys.stdin.readline().strip().split()
        score = float(read[1])
        grade = get_gpa(read[2])
        if grade != -1:
            sum_score += score * grade
            sum_grade += score
    if sum_grade == 0:
        print(0)
    else:
        print(sum_score / sum_grade)


sol()
