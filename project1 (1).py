class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.parked_vehicles = {}

    def vehicle_entry(self, vehicle_no):
        if len(self.parked_vehicles) < self.total_spots:
            self.parked_vehicles[vehicle_no] = 0
            print("Vehicle Entered:", vehicle_no)
        else:
            print("Parking Full!")

    def vehicle_exit(self, vehicle_no, hours):
        if vehicle_no in self.parked_vehicles:
            fee = hours * 20
            del self.parked_vehicles[vehicle_no]
            print("Vehicle Exit:", vehicle_no)
            print("Parking Fee:", fee)
        else:
            print("Vehicle not found")

    def available_spots(self):
        print("Available Spots:", self.total_spots - len(self.parked_vehicles))


def main():
    p = ParkingLot(5)

    while True:
        print("\n1.Entry 2.Exit 3.Available Spots 4.Exit Program")
        choice = int(input("Enter choice: "))

        if choice == 1:
            v = input("Enter Vehicle Number: ")
            p.vehicle_entry(v)

        elif choice == 2:
            v = input("Enter Vehicle Number: ")
            h = int(input("Enter Hours Parked: "))
            p.vehicle_exit(v, h)

        elif choice == 3:
            p.available_spots()

        elif choice == 4:
            break


main()