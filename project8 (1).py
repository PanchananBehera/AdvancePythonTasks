class Warehouse:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty):
        self.items[name] = qty

    def move_item(self, name, qty):
        if name in self.items:
            self.items[name] -= qty

    def report(self):
        print("Inventory Report:")
        for item, qty in self.items.items():
            print(item, ":", qty)

w = Warehouse()

w.add_item("Laptop", 10)
w.add_item("Phone", 20)

w.move_item("Laptop", 2)

w.report()