class Freelancer:
    def __init__(self, name):
        self.name = name

class Client:
    def __init__(self, name):
        self.name = name

class Project:
    def __init__(self, title, freelancer, client, payment):
        self.title = title
        self.freelancer = freelancer
        self.client = client
        self.payment = payment

    def show_project(self):
        print("Project:", self.title)
        print("Freelancer:", self.freelancer.name)
        print("Client:", self.client.name)
        print("Payment:", self.payment)

f = Freelancer("Ali")
c = Client("Sara")

p = Project("Website Design", f, c, 200)
p.show_project()