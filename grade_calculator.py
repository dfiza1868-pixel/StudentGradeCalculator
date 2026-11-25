def total_marks(marks):
    return sum(marks)


def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def is_pass(marks):
    return all(mark >= 35 for mark in marks)


def main():
    print("STUDENT GRADE CALCULATOR")

    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total = total_marks(marks)
    avg = average(marks)
    result_grade = grade(avg)
    result = is_pass(marks)

    print("\n----- RESULT -----")
    print("Total Marks:", total)
    print("Average:", avg)
    print("Grade:", result_grade)
    print("Result:", "PASS" if result else "FAIL")


if __name__ == "__main__":
    main()