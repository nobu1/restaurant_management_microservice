from admin_manage import Admin
from customer_manage import Customer
import csv
import getpass

ADMIN_LOGIN_DATA = "./csv/admin_login_data.csv"
CUSTOMER_LOGIN_DATA_ID = "./csv/customer_login_data_id.csv"
CUSTOMER_LOGIN_DATA_PHONE = "./csv/customer_login_data_phone.csv"
CUSTOMERS_DATA = "./csv/customers_data.csv"


class Login:

    def show_login_page(self):
        print("----------------------------------------")
        print("Welcome to Restaurant Management System!")
        print("----------------------------------------")
        print("\n")
        print("This program analyzes restaurants data to create "
              "strategy for enhancing sales.")
        print("Admin confirm customers and reservations profiles graphically.")
        print("\n")

        while True:
            print("Which account do you want to log in with?")
            print("1. Administrator account")
            print("2. Customers account")
            print("3. Create customer account")
            print("4. Quit the program")
            user_input = input(
                "Enter which account log in with a number[1-4]: "
            )
            print("\n")

            login_count = 0
            login = Login()
            if user_input == "1":
                # Admin login
                login.admin_login(login_count)
            elif user_input == "2":
                # Customer login
                login.customer_login(login_count)
            elif user_input == "3":
                # Create customer account
                login.create_customer_account()
            elif user_input == "4":
                print("Goodbye!")
                break
            else:
                print("Please input a number between 1 and 3.")
                print("\n")

    def admin_login(self, login_count):
        print("Administrator Login Page")
        print("Please input ID and passowrd")
        id = input("ID(Required): ")
        password = getpass.getpass(prompt="Password(Required): ")
        print("\n")

        # Read admin_login_data.csv
        with open(
            ADMIN_LOGIN_DATA,
            "r",
            encoding="ms932"
        ) as csv_file:
            f = csv.reader(
                csv_file, delimiter=",", doublequote=True,
                lineterminator="\r\n", quotechar='"', skipinitialspace=True
            )
            next(f)
            csv_id = ""
            csv_password = ""
            for row in f:
                csv_id = row[0]
                csv_password = row[1]

        # Check login input data
        if (id == csv_id) and (password == csv_password):
            admin = Admin()
            admin.admin_menu()
        else:
            login = Login()
            print("Incorrect ID or Password")
            login_count += 1

            # Exceeded login attempt
            if login_count > 3:
                print("Exceeded login attempt! Go back to login page.")
                print("\n")
                login.show_login_page()

            print("Try again")
            print("\n")
            return login.admin_login(login_count)

        return

    def customer_login(self, login_count):
        print("Customer Login Page")
        print("Which method do you log in?")

        method = 0
        while True:
            print("1. Login with ID")
            print("2. Login with Phone Number")
            method = input(
                    "Enter the method with a number[1-2]: "
            )
            print("\n")

            id = 0
            if method == "1":
                # Login with ID
                print("Please input ID and passowrd")
                id = input("ID(Required): ")
                break
            elif method == "2":
                # Login with Phone Number
                print("Please input Phone Number and passowrd")
                id = input("Phone Number(Required): ")
                break
            else:
                print("Please input a number between 1 and 2.")
                print("\n")

        password = getpass.getpass(prompt="Password(Required): ")
        print("\n")

        # Read customer_login_data_id/phone.csv
        if method == "1":
            # Login with ID
            with open(
                CUSTOMER_LOGIN_DATA_ID,
                "r",
                encoding="ms932"
            ) as csv_file:
                f = csv.reader(
                    csv_file, delimiter=",", doublequote=True,
                    lineterminator="\r\n", quotechar='"', skipinitialspace=True
                )
                next(f)
                csv_id = ""
                csv_password = ""
                for row in f:
                    csv_id = row[0]
                    csv_password = row[1]
        else:
            # Login with Phone
            with open(
                CUSTOMER_LOGIN_DATA_PHONE,
                "r",
                encoding="ms932"
            ) as csv_file:
                f = csv.reader(
                    csv_file, delimiter=",", doublequote=True,
                    lineterminator="\r\n", quotechar='"', skipinitialspace=True
                )
                next(f)
                csv_id = ""
                csv_password = ""
                for row in f:
                    csv_id = row[0]
                    csv_password = row[1]

        # Check login input data
        if (id == csv_id) and (password == csv_password):
            customer = Customer()
            customer.customer_menu()
        else:
            login = Login()
            print("Incorrect ID or Phone or Password")
            login_count += 1

            # Exceeded login attempt
            if login_count > 3:
                print("Exceeded login attempt! Go back to login page.")
                print("\n")
                login.show_login_page()

            print("Try again")
            print("\n")
            return login.customer_login(login_count)

        return

    def create_customer_account(self):
        print("---------- Create your account ----------")
        print("Find your favorite restaurants!")
        print("Reserve your favorite restaurant with date, "
              "time, and number of people.")

        confirmation = input("Do you create a new account?[y/n]: ")
        if confirmation.lower() != "y":
            print("OK, we hope to visit next time, Bye!")
            print("\n")
            return

        name = input("Name(Required): ")
        gender = input("Gender(Male/Female Optional): ")
        age = input("Age(Required): ")
        email = input("Email(Required): ")
        phone = input("Phone number(Required): ")
        address = input("Address(Required): ")

        password = input("Password(Required): ")

        # Write customer_login_data_id.csv
        with open(
            CUSTOMER_LOGIN_DATA_ID,
            "a",
            encoding="ms932"
        ) as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow([email, password])

        # Write customers_login_data_phone.csv
        with open(
            CUSTOMER_LOGIN_DATA_PHONE,
            "a",
            encoding="ms932"
        ) as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow([phone, password])

        # Write customers_data.csv
        with open(
            CUSTOMERS_DATA,
            "a",
            encoding="ms932"
        ) as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow([
                name,
                gender,
                age,
                email,
                phone,
                address
            ])
        print("Create your account successfully!")
        print("\n")
        return
