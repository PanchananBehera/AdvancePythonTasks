class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_gpa(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 90:
            return 10
        elif avg >= 80:
            return 9
        elif avg >= 70:
            return 8
        elif avg >= 60:
            return 7
        else:
            return 6


class ResultSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")

        marks = []
        for i in range(3):
            m = int(input("Enter marks of subject: "))
            marks.append(m)

        s = Student(name, marks)
        self.students.append(s)

    def show_results(self):
        print("\nStudent Results")
        for s in self.students:
            gpa = s.calculate_gpa()
            print("Name:", s.name)
            print("Marks:", s.marks)
            print("GPA:", gpa)
            print("------------------")


def main():
    r = ResultSystem()

    while True:
        print("\n1. Add Student Marks")
        print("2. Show Result")
        print("3. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            r.add_student()

        elif ch == 2:
            r.show_results()

        elif ch == 3:
            break


main()