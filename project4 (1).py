class MovieBooking:
    def __init__(self):
        self.movies = {
            "Avengers": ["10AM", "2PM", "6PM"],
            "Batman": ["11AM", "3PM", "7PM"]
        }

        self.seats = ["A1","A2","A3","A4","A5"]

    def show_movies(self):
        print("\nAvailable Movies and Showtimes:")
        for movie, time in self.movies.items():
            print(movie, ":", time)

    def book_ticket(self):
        movie = input("Enter movie name: ")
        time = input("Enter showtime: ")

        print("Available Seats:", self.seats)

        seat = input("Select seat: ")

        if seat in self.seats:
            self.seats.remove(seat)
            print("\nTicket Booked Successfully")
            print("Movie:", movie)
            print("Showtime:", time)
            print("Seat:", seat)
        else:
            print("Seat not available")

def main():
    m = MovieBooking()

    while True:
        print("\n1. Show Movies")
        print("2. Book Ticket")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            m.show_movies()

        elif choice == 2:
            m.book_ticket()

        elif choice == 3:
            break

main()