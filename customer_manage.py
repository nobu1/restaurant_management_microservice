import csv

RESERVATION = "./csv/reservation_data.csv"


class Customer:

    def customer_menu(self):
        while True:
            print("Please select following menu")
            print("1. Reserve restaurant")
            print("2. Show help page")
            print("3. Logout")
            customer_input = input(
                "Enter the menu number[1-3]: "
            )
            print("\n")

            if customer_input == "1":
                customer_name = input("Your name: ")
                reservation_date = input("Reservation Date(YYYY-MM-DD): ")
                reservation_time = input("Reservation time(XX:XX): ")
                number_people = input("Number of people: ")
                reservation = [
                    customer_name,
                    reservation_date,
                    reservation_time,
                    number_people
                ]

                # Write reservation.csv
                with open(
                    RESERVATION,
                    "a",
                    encoding="ms932"
                ) as csv_file:
                    writer = csv.writer(csv_file, lineterminator='\n')
                    writer.writerow(reservation)

                print("Reservation completed!")
                print("\n")

            elif customer_input == "2":
                print("After access to the reservation page, the reservation "
                      "procedure is as follows.")
                print("1. Confirm the restaurant name and "
                      "address on the list.")
                print("2. Input your name.")
                print("3. Input the reservation date and time.")
                print("4. Input the number of people.")
                print("\n")
            elif customer_input == "3":
                print("Logout successfully. Bye")
                print("\n")
                break
            else:
                print("Please input a number between 1 and 3.")
                print("\n")

        return
