import zmq


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
                microserviceB = MicroserviceB()
            elif microservice_input == "3":
                microserviceC = MicroserviceC()
            elif microservice_input == "4":
                microserviceD = MicroserviceD()
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
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:30000")

        customer_name = input("Enter the customer name@: ")
        request_reservation_json = {
            "request": {
                "event": "reservationData",
                "body": {
                    "customerName": customer_name
                }
            }
        }
        socket.send_json(request_reservation_json)

        recv_message = socket.recv_string()
        print("Receive message = %s" % recv_message)

        socket.close()
        context.destroy()

        return
