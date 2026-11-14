# Student Data Manager Using Files
# Create the file automatically if it does not exist
open("students.txt", "a").close()
# 1. Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    if not roll.strip() or not name.strip() or not course.strip():
        print("All fields are required!")
        return
 if "," in roll or "," in name or "," in course:
        print("Commas are not allowed!")
        return
    with open("students.txt", "r") as file:
        records = file.readlines()
    for record in records:
        data = record.strip().split(",", 2)
        if data[0] == roll:
            print("Roll number already exists!")
            return
    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + course + "\n")
    print("Student added successfully!")
# 2. Display Students
def display_students():
    print("\n--- Student Records ---")
    with open("students.txt", "r") as file:
        records = file.readlines()
    if not records:
        print("No student records found.")
        return
  for record in records:
        data = record.strip().split(",", 2)
    print("Roll Number:", data[0])
        print("Name:", data[1])
        print("Course:", data[2])
        print("----------------------")
# 3. Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")
  with open("students.txt", "r") as file:
        for record in file:
            data = record.strip().split(",", 2)
            if data[0] == roll:
                print("\nStudent Found!")
                print("Roll Number:", data[0])
                print("Name:", data[1])
                print("Course:", data[2])
                return
    print("Student not found!")
# 4. Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")
    with open("students.txt", "r") as file:
        records = file.readlines()
    found = False
    updated_records = []
    for record in records:
        data = record.strip().split(",", 2)
        if data[0] == roll:
            found = True
            new_name = input("Enter New Name: ")
            new_course = input("Enter New Course: ")
            if not new_name.strip() or not new_course.strip():
                print("Fields cannot be empty!")
 return
 if "," in new_name or "," in new_course:
                print("Commas are not allowed!")
                return
            updated_records.append(
                roll + "," + new_name + "," + new_course + "\n"
            )
        else:
            updated_records.append(record)
    if found:
        with open("students.txt", "w") as file:
            file.writelines(updated_records)
        print("Student record updated successfully!")
    else:
        print("Student not found!")
# Main Menu
while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Program exited successfully!")
        break
    else:
        print("Invalid choice! Please enter 1-5.")

