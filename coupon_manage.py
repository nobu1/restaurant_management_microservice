import csv
import pandas as pd


COUPON_DATA = "./csv/coupons_data.csv"


class Coupon:

    def coupon_menu(self):
        while True:
            print("Please select following menu")
            print("1. Show coupons data")
            print("2. Add coupon data")
            print("3. Edit coupon data")
            print("4. Back to admin page")
            coupon_input = input(
                "Enter the menu number[1-4]: "
            )
            print("\n")

            if coupon_input == "1":
                # Show coupon data
                print("---------- Coupons Data ----------")
                with open(
                    COUPON_DATA,
                    "r",
                    encoding="ms932"
                ) as csv_file:
                    f = csv.reader(
                        csv_file, delimiter=",", doublequote=True,
                        lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True
                    )
                    header = next(f)
                    print(header)
                    for row in f:
                        print(row)
                print("\n")
            elif coupon_input == "2":
                # Display time consuming reason
                print("Before creating new coupon data, you must confirm "
                      "the correctness of the data to the department"
                      " in charge.")
                print("Normally, it takes 2 weeks for the confirmation.")

                # Set adding data
                id = input("Coupon ID(Required): ")
                name = input("Coupon name(Required): ")
                print("Please input the type number")
                type = 0
                while True:
                    print("1: Percent")
                    print("2: Price")
                    type = input("Enter the type number[1-2]: ")
                    if type == "1" or type == "2":
                        break
                    else:
                        print("Please input a number between 1 and 2.")
                        print("\n")
                type_str = ""
                if type == "1":
                    type_str = "Percent"
                elif type == "2":
                    type_str = "Price"
                amount = input("Amount(Required): ")
                valid_date = input("Valid Date(Required YYYY-MM-DD): ")

                # Add coupon data into coupons_data.csv
                df = pd.DataFrame({
                    'ID': [id],
                    'Name': [name],
                    'Type': [type_str],
                    'Amount': [amount],
                    'ValidDate': [valid_date]
                })
                df.to_csv(COUPON_DATA, index=False, mode='a', header=False)
                print("The coupon data is added.")
                print("\n")
            elif coupon_input == "3":
                # Set coupon ID
                coupon_id = input("Enter the modified coupon ID: ")
                coupon_id = int(coupon_id) - 1

                # Read coupons_data.csv
                df = pd.read_csv(COUPON_DATA)

                # Update coupon name
                update = input("Do you edit the coupon name? [y/n]: ")
                if update.lower() == "y":
                    name = input("Update the coupon name: ")
                    df.loc[coupon_id, "Name"] = name

                # Update Type
                update = input("Do you edit the coupon type? [y/n]: ")
                if update.lower() == "y":
                    type = 0
                    while True:
                        print("1: Percent")
                        print("2: Price")
                        type = input("Enter the type number[1-2]: ")
                        if type == "1":
                            df.loc[coupon_id, "Type"] = "Percent"
                            break
                        elif type == "2":
                            df.loc[coupon_id, "Type"] = "Price"
                            break
                        else:
                            print("Please input a number between 1 and 2.")
                            print("\n")

                # Update amount
                update = input("Do you edit the amount? [y/n]: ")
                if update.lower() == "y":
                    amount = input("Update the amount: ")
                    df.loc[coupon_id, "Amount"] = amount

                # Update valid date
                update = input("Do you edit the valid date? [y/n]: ")
                if update.lower() == "y":
                    valid_date = input("Update the valid date: ")
                    df.loc[coupon_id, "ValidDate"] = valid_date

                # Edit coupon data
                df.to_csv(COUPON_DATA, index=False)
                print("The coupon data is updated.")
                print("\n")
            elif coupon_input == "4":
                # Back to admin page
                print("Go back to admin page")
                print("\n")
                break
            else:
                print("Please input a number between 1 and 4.")
                print("\n")
        return
