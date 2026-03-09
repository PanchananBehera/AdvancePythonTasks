class Task:
    def __init__(self, name, category, deadline, priority):
        self.name = name
        self.category = category
        self.deadline = deadline
        self.priority = priority


class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Task Name: ")
        category = input("Category: ")
        deadline = input("Deadline: ")
        priority = input("Priority: ")

        task = Task(name, category, deadline, priority)
        self.tasks.append(task)
        print("Task Added!")

    def show_tasks(self):
        for t in self.tasks:
            print(t.name, "|", t.category, "|", t.deadline, "|", t.priority)

    def filter_category(self):
        cat = input("Enter category to filter: ")
        for t in self.tasks:
            if t.category == cat:
                print(t.name, "|", t.deadline, "|", t.priority)


def main():
    manager = TodoManager()

    while True:
        print("\n1.Add Task 2.Show Tasks 3.Filter Category 4.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            manager.add_task()

        elif ch == 2:
            manager.show_tasks()

        elif ch == 3:
            manager.filter_category()

        elif ch == 4:
            break


main()