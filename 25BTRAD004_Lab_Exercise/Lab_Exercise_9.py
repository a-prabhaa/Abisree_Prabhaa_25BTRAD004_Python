students = {} n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    while True:         marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break         else:             print("Invalid marks! Enter marks between 0 and 100.")     students[name] = marks print("\n--- STUDENT RESULTS ---") for name, marks in students.items():
    if marks >= 90:         grade = "A"     elif marks >= 80:         grade = "B"     elif marks >= 70:         grade = "C"	OUTPUT:     elif marks >= 60:         grade = "D"     elif marks >= 40:         grade = "E"     else:         grade = "F"     result = "Pass" if marks >= 40 else "Fail"
    print("Name:", name)     print("Marks:", marks)     print("Grade:", grade)     print("Result:", result)     print("-------------------")
