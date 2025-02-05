from admin_manage import Admin
from customer_manage import Customer


def main():
    print("----------------------------------------")
    print("Welcome to Restaurant Management System!")
    print("----------------------------------------")
    print("\n")
    print("This program analyzes restaurants data to create strategy for enhancing sales.")
    print("Admin confirm customers and reservations profiles graphically.")
    print("\n")
    
    user_input = 0

    while user_input != 3:
        print("Which account do you want to log in with?")
        print("1. Administrator account")
        print("2. Customers account")
        print("3. Quit the program")
        user_input = input("Enter which account log in with a number[1-3]: ")

        if user_input == "1":
            Admin.managementPage()

        elif user_input == "2":
            Customer.managementPage()
            
        elif user_input == "3":
            print("Goodbye!")
            break
        else:
            print("Please input a number between 1 and 3.")
            print("\n")

if __name__ == '__main__':
    main()
    