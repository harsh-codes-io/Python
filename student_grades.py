students_grade = {"Alice":92,"Emily":96,"Ryan":90}

# Print the name of student scored highest
print(max(students_grade,key = students_grade.get))

#Find average mark of class
average_marks = (sum(students_grade.values())) / len(students_grade)

#print name of students scoring above average
print(f"\n\n Students scored above average({average_marks}): ")
for name,marks in students_grade.items():
    if marks > average_marks:
        print(name)