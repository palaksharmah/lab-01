students = []
def add_student(name, roll_no):
    student = {"Name": name, "Roll": roll_no}
    students.append(student)
    print(f"Student {name} added successfully!")
def display_students():
    if not students:
        print("\nNo students in the record.")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"Name: {s['Name']}, Roll No: {s['Roll']}")
add_student("Aparna", "101")
add_student("Bob", "102")
display_students()