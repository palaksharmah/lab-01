# List to store student records
students = []

def add_student(name, roll_no):
    # Create a simple dictionary for the student
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

# --- Testing the system ---
add_student("Alice", "101")
add_student("Bob", "102")
display_students()