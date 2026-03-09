class Store:
    def __init__(self):
        self.products = {
            "milk": 40,
            "bread": 30,
            "egg": 10,
            "rice": 60
        }
        self.cart = []

    def show_products(self):
        print("\nAvailable Products:")
        for p, price in self.products.items():
            print(p, ":", price)

    def add_product(self):
        item = input("Enter product name: ")

        if item in self.products:
            qty = int(input("Enter quantity: "))
            self.cart.append((item, qty))
        else:
            print("Product not found")

    def generate_bill(self):
        total = 0

        print("\n----- BILL -----")

        for item, qty in self.cart:
            price = self.products[item]
            cost = price * qty
            total += cost
            print(item, qty, cost)

        discount = 0
        if total > 200:
            discount = total * 0.10

        final = total - discount

        print("Total:", total)
        print("Discount:", discount)
        print("Final Amount:", final)


def main():
    s = Store()

    while True:
        print("\n1.Show Products 2.Add Product 3.Generate Bill 4.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            s.show_products()

        elif ch == 2:
            s.add_product()

        elif ch == 3:
            s.generate_bill()

        elif ch == 4:
            break


main()