



students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        for student in students:
            print(student)

    elif choice == "3":
        search_roll = input("Enter roll number: ")

        for student in students:
            if student["roll"] == search_roll:
                print(student)
                break
        else:
            print("Student not found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")