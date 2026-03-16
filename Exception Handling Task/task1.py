class EmptyInputError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

grades = {}  # student_id: grade

def add_or_update_grade():
    try:
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            raise EmptyInputError("Student ID cannot be empty.")
        grade_input = input("Enter grade (0-100): ").strip()
        if not grade_input:
            raise EmptyInputError("Grade cannot be empty.")
        grade = float(grade_input)
        if not 0 <= grade <= 100:
            raise InvalidGradeError("Grade must be between 0 and 100.")
        grades[student_id] = grade
        print(f"Grade for {student_id} set to {grade}.")
    except ValueError:
        print("Error: Invalid number format for grade.")
    except EmptyInputError as e:
        print(f"Error: {e}")
    except InvalidGradeError as e:
        print(f"Error: {e}")

def delete_grade():
    try:
        student_id = input("Enter student ID to delete: ").strip()
        if not student_id:
            raise EmptyInputError("Student ID cannot be empty.")
        if student_id in grades:
            del grades[student_id]
            print(f"Grade for {student_id} deleted.")
        else:
            raise KeyError("Student not found.")
    except KeyError as e:
        print(f"Error: {e}")
    except EmptyInputError as e:
        print(f"Error: {e}")

def view_grades():
    if not grades:
        print("No grades recorded.")
    else:
        for sid, g in grades.items():
            print(f"{sid}: {g}")

while True:
    print("\n1. Add/Update Grade  2. Delete Grade  3. View Grades  4. Exit")
    choice = input("Choose: ").strip()
    if choice == '1':
        add_or_update_grade()
    elif choice == '2':
        delete_grade()
    elif choice == '3':
        view_grades()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
