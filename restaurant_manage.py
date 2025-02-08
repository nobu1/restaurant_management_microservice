import csv
import pandas as pd


RESTAURANT_DATA = "./csv/restaurants_data.csv"


class Restaurant:

    def restaurant_menu(self):
        while True:
            print("Please select following menu")
            print("1. Show restaurants data")
            print("2. Add restaurant data")
            print("3. Edit restaurant data")
            print("4. Delete restaurant data")
            print("5. Back to admin page")
            restaurant_input = input(
                "Enter the menu number[1-5]: "
            )
            print("\n")

            if restaurant_input == "1":
                # Show restaurant data
                print("---------- Restaurants Data ----------")
                with open(
                    RESTAURANT_DATA,
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
            elif restaurant_input == "2":
                # Display time consuming reason
                print("Before creating new restaurant data, you must confirm "
                      "the correctness of the data to the department"
                      " in charge.")
                print("Normally, it takes 2 weeks for the confirmation.")

                # Set adding data
                id = input("Restaurant ID(Required): ")
                name = input("Restaurant name(Required): ")
                address = input("Restaurant address(Required): ")
                print("Please input the status number")
                status = 0
                while True:
                    print("1: Open")
                    print("2: Under Renovation")
                    print("3: Opening Preparation")
                    status = input("Enter the status number[1-3]: ")
                    if status == "1" or status == "2" or status == "3":
                        break
                    else:
                        print("Please input a number between 1 and 3.")
                        print("\n")
                status_str = ""
                if status == "1":
                    status_str = "Open"
                elif status == "2":
                    status_str == "Under Renovation"
                elif status == "3":
                    status_str == "Opening Preparation"

                # Add restaurant data into restaurants_data.csv
                df = pd.DataFrame({
                    'ID': [id],
                    'Name': [name],
                    'Address': [address],
                    'Status': [status_str]
                })
                df.to_csv(RESTAURANT_DATA, index=False, mode='a', header=False)
                print("The restaurant data is added.")
                print("\n")
            elif restaurant_input == "3":
                # Set restaurant ID
                restaurant_id = input("Enter the modified restaurant ID: ")
                restaurant_id = int(restaurant_id) - 1

                # Read restanrauts_data.csv
                df = pd.read_csv(RESTAURANT_DATA)

                # Update restaurant name
                update = input("Do you edit the restaurant name? [y/n]: ")
                if update.lower() == "y":
                    name = input("Update the restaurant name: ")
                    df.loc[restaurant_id, "Name"] = name

                # Update address
                update = input("Do you edit the restaurant address? [y/n]: ")
                if update.lower() == "y":
                    address = input("Update the restaurant address: ")
                    df.loc[restaurant_id, "Address"] = address

                # Update status
                update = input("Do you edit the restaurant status? [y/n]: ")
                if update.lower() == "y":
                    status = 0
                    while True:
                        print("1: Open")
                        print("2: Under Renovation")
                        print("3: Opening Preparation")
                        status = input("Enter the status number[1-3]: ")
                        if status == "1":
                            df.loc[restaurant_id, "Status"] = "Open"
                            break
                        elif status == "2":
                            df.loc[restaurant_id, "Status"] = \
                                "Under Renovation"
                            break
                        elif status == "3":
                            df.loc[restaurant_id, "Status"] = \
                                "Opening Preparation"
                            break
                        else:
                            print("Please input a number between 1 and 3.")
                            print("\n")

                # Edit restaurant data
                df.to_csv(RESTAURANT_DATA, index=False)
                print("The restaurant data is updated.")
                print("\n")
            elif restaurant_input == "4":
                # Set restaurant ID
                restaurant_id = input("Enter the deleting restaurant ID: ")
                restaurant_id = int(restaurant_id) - 1

                # Show delete confirmation message
                confirmation = input(
                    "Do you delete the restaurant(restaurant_id = " +
                    restaurant_id +
                    ")?[y/n] "
                )

                if confirmation.lower() == "y":
                    # Delete restaurant data
                    df = pd.read_csv(RESTAURANT_DATA)
                    df = df.drop(index=restaurant_id)
                    df.to_csv(RESTAURANT_DATA, index=False)
                    print("The selected restaurant is deleted.")
                else:
                    # Cancel delete method
                    print("The deletion process is canceled.")
                print("\n")
            elif restaurant_input == "5":
                # Back to admin page
                print("Go back to admin page")
                print("\n")
                break
            else:
                print("Please input a number between 1 and 5.")
                print("\n")

        return
