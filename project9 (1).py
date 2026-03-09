class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logs = []

    def add_log(self, message):
        self.logs.append(message)

    def show_logs(self):
        print("Customer:", self.name)
        for log in self.logs:
            print("-", log)

c1 = Customer("John", "john@email.com")

c1.add_log("Called about product")
c1.add_log("Interested in buying")

c1.show_logs()