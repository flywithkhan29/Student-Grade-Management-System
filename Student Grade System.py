# Student Grade Management System

students = []  

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = [] 
    for j in range(3):
        mark = int(input(f"Enter mark {j+1} for {name}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)

    
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'

    
    student_data = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }
    students.append(student_data)


print("\n----- Student Report -----")
for student in students:
    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Total: {student['total']} | Average: {student['average']:.2f} | Grade: {student['grade']}")
    print("-------------------------")

