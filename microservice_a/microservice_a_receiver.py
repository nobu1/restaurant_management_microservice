import zmq
import csv
import pandas as pd


CUSTOMER_DATA = "../csv/customers_data.csv"


class MicroserviceA:

    def reservaion_records(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:30000")

        print("Reservation Records Receiver Startup.")

        while True:
            reservation_records = socket.recv_json()

            # Request message validation
            event = reservation_records['request']['event']
            if event == "reservationData":
                customer_name = reservation_records['request']\
                    ['body']['customerName']

                # Extract customer data from customer_data.csv
                
            else:
                response_json = {
                    "request": {
                        "event": "reservationDataError",
                        "body": {}
                    }
                } 

            socket.send_json(response_json)

        socket.close()
        context.destroy()
