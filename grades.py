def get_topper(marks: dict[str,int]) -> str | None:
    if not marks:
        return None
    else:
        return max(marks, key=marks.get)


def get_average(marks: dict[str,int]) -> float:
    return sum(marks.values())/len(marks)


def get_above_average(marks: dict[str,int], avg: float) -> list[str]:
    students = []
    item = marks.items()
    for i in item:
        if i[1] >avg:
            students.append(i[0])

    return students


def print_report(marks: dict[str,int]) -> None:
    print(get_topper(marks))
    avg = get_average(marks)
    print(avg)
    print(get_above_average(marks,avg))


if __name__ == "__main__":
    students_grade = {"Alice":92,"Emily":96,"Ryan":90,"bob":95}
    print_report(students_grade)
   
