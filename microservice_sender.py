import zmq
from .microservice_a.microservice_a_receiver import MicroserviceA
from .microservice_b.microservice_b_receiver import MicroserviceB
from .microservice_c.microservice_c_receiver import MicroserviceC
from .microservice_d.microservice_d_receiver import MicroserviceD


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
                # Start Microservice A receiver
                microserviceA = MicroserviceA()
                microserviceA.reservaion_records()

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
        return
