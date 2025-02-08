from restaurant_manage import Restaurant
from coupon_manage import Coupon
from microservice_sender import MicroserviceSender
import csv


CUSTOMERS_DATA = "./csv/customers_data.csv"
RESERVATION_DATA = "./csv/reservation_data.csv"


class Admin:

    def admin_menu(self):
        while True:
            print("Please select following menu")
            print("1. Show management data")
            print("2. Show customers data")
            print("3. Manage restaurants data")
            print("4. Show reservations data")
            print("5. Manage coupons data")
            print("6. Logout")
            admin_input = input(
                "Enter the menu number[1-6]: "
            )
            print("\n")

            admin = Admin()
            if admin_input == "1":
                microserviceSender = MicroserviceSender()
                microserviceSender.microservice_menu()
            elif admin_input == "2":
                # Show customers data
                admin.show_customers()
            elif admin_input == "3":
                # Manage restaurants data
                restaurant = Restaurant()
                restaurant.restaurant_menu()
            elif admin_input == "4":
                # Show reservations data
                admin.show_reservations()
            elif admin_input == "5":
                # Manage coupons data
                coupon = Coupon()
                coupon.coupon_menu()
            elif admin_input == "6":
                # Logout
                print("Logout successfully. Bye")
                print("\n")
                break
            else:
                print("Please input a number between 1 and 6.")
                print("\n")

        return

    def show_customers(self):
        print("---------- Customers Data ----------")
        # Open customers_data.csv
        with open(
            CUSTOMERS_DATA,
            "r",
            encoding="ms932"
        ) as csv_file:
            f = csv.reader(
                csv_file, delimiter=",", doublequote=True,
                lineterminator="\r\n", quotechar='"', skipinitialspace=True
            )
            header = next(f)
            print(header)
            for row in f:
                print(row)
        print("\n")

        return

    def show_reservations(self):
        print("---------- Reservations Data ----------")
        # Open reservation_data.csv
        with open(
            RESERVATION_DATA,
            "r",
            encoding="ms932"
        ) as csv_file:
            f = csv.reader(
                csv_file, delimiter=",", doublequote=True,
                lineterminator="\r\n", quotechar='"', skipinitialspace=True
            )
            header = next(f)
            print(header)
            for row in f:
                print(row)
        print("\n")

        return
