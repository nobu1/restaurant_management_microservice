import zmq
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

RESERVATION_DATA = "./csv/reservation_data.csv"


class MicroserviceSender:

    def microservice_menu(self):
        while True:
            print("Please select following menu")
            print("1. Analyze reservation data")
            print("2. Analyze customers data")
            print("3. Analyze coupons data")
            print("4. Analyze restaurants data")
            print("5. Back to admin page")
            microservice_input = input(
                "Enter the menu number[1-5]: "
            )
            print("\n")

            microserviceSender = MicroserviceSender()
            if microservice_input == "1":
                # Start Microservice A sender
                microserviceSender.microservice_a_sender()
            elif microservice_input == "2":
                microserviceSender.microservice_b_sender()
            elif microservice_input == "3":
                microserviceSender.microservice_c_sender()
            elif microservice_input == "4":
                microserviceSender.microservice_d_sender()
            elif microservice_input == "5":
                # Back to admin page
                print("Go back to admin page")
                print("\n")
                break
            else:
                print("Please input a number between 1 and 5.")
                print("\n")

        return

    def microservice_a_sender(self):
        # Show unique customers
        df = pd.read_csv(RESERVATION_DATA)
        customers = df["Name"].unique()
        print("Input 5 customers name(Empty OK): ")
        print(customers)

        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:30000")

        # Send request json
        reservation_records = {}
        for i in range(5):
            customer_name = input("Enter the customer name: ")
            request_reservation_json = {
                "request": {
                    "event": "reservationData",
                    "body": {
                        "customerName": customer_name
                    }
                }
            }
            socket.send_json(request_reservation_json)

            # Extract JSON response
            receive_reservaion_json = socket.recv_json()
            reservation_count = 0
            histories = receive_reservaion_json['response']['body']['history']
            for _ in histories:
                reservation_count += 1

            # Store reservation count by user
            reservation_records[customer_name] = reservation_count

        # Show results of analyzed reservation
        x_data = reservation_records.keys()
        y_data = reservation_records.values()
        plt.yticks(range(0, max(y_data) + 1, 1))
        plt.bar(x_data, y_data, align="center")
        plt.ylabel("Reservation Counts")
        plt.xlabel("Customers Name")
        plt.title("Reservation Trends by customers")
        plt.show()

        socket.close()
        context.destroy()

        return

    def microservice_b_sender(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:30001")

        # Send request json
        request_reservation_json = {
            "request": {
                "event": "customerAgeData",
                "body": {}
            }
        }
        socket.send_json(request_reservation_json)

        # Extract JSON response
        receive_customer_age_json = socket.recv_json()
        customer_ages = {
            "10s": 0,
            "20s": 0,
            "30s": 0,
            "40s": 0,
            "Over50s": 0
        }
        for age in (
            receive_customer_age_json["response"]["body"]["customerAge"]
        ):
            if int(age) < 20:
                customer_ages["10s"] += 1
            elif 20 <= int(age) < 30:
                customer_ages["20s"] += 1
            elif 30 <= int(age) < 40:
                customer_ages["30s"] += 1
            elif 40 <= int(age) < 50:
                customer_ages["40s"] += 1
            elif int(age) >= 50:
                customer_ages["Over50s"] += 1
        print(customer_ages)
        # Show results of analyzed customer ages
        ages = np.array(list(customer_ages.values()))
        label = list(customer_ages)
        plt.pie(
            ages,
            labels=label,
            counterclock=False,
            startangle=90,
            autopct="%1.1f%%"
        )
        plt.title("Customers Age Profile")
        plt.show()

        return

    def microservice_c_sender(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:30002")

        # Input start and end period
        print("Input start and end period(Required)")
        start = input("Start period(Required YYYY-MM-DD): ")
        end = input("End period(Required YYYY--MM-DD): ")

        # Send request json
        request_coupon_json = {
            "request": {
                "event": "couponData",
                "body": {
                    "startPeriod": start,
                    "endPeriod": end
                }
            }
        }
        socket.send_json(request_coupon_json)

        # Extract JSON response
        receive_coupon_json = socket.recv_json()
        coupons_records = {
            "Percent": receive_coupon_json["response"]["body"]["Percent"],
            "Price": receive_coupon_json["response"]["body"]["Price"]
        }
        # Show results of analyzed coupon
        x_data = coupons_records.keys()
        y_data = coupons_records.values()
        plt.yticks(range(0, max(y_data) + 1, 1))
        plt.bar(x_data, y_data, align="center")
        plt.ylabel("Coupon Category Counts")
        plt.xlabel("Coupon Type")
        plt.title("Coupon Profile")
        plt.show()

        return

    def microservice_d_sender(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:30003")

        # Send request json
        request_restaurant_json = {
            "request": {
                "event": "restaurantData",
                "body": {}
            }
        }
        socket.send_json(request_restaurant_json)

        # Extract JSON response
        receive_restaurant_status_json = socket.recv_json()
        restaurant_status = {
            "Open": 0,
            "Under Renovation": 0,
            "Opening Preparation": 0,
        }
        restaurant_status['Open'] = \
            receive_restaurant_status_json["response"]["body"]["Open"]
        restaurant_status['Under Renovation'] = \
            receive_restaurant_status_json["response"]["body"][
                "Under Renovation"
            ]
        restaurant_status['Opening Preparation'] = \
            receive_restaurant_status_json["response"]["body"][
                "Opening Preparation"
            ]

        # Show results of analyzed restaurant status
        stauts_counts = np.array(list(restaurant_status.values()))
        label = list(restaurant_status.keys())
        plt.pie(
            stauts_counts,
            labels=label,
            counterclock=False,
            startangle=90,
            autopct="%1.1f%%"
        )
        plt.title("Restaurant Stauts Profile")
        plt.show()

        return
