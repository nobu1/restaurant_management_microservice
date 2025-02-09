import zmq
import pandas as pd


CUSTOMER_DATA = "../csv/customers_data.csv"


def customer_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:30001")

    print("Customer Records Receiver Startup.")

    while True:
        # Receive JSON request
        customer_records = socket.recv_json()

        # Confirm event data
        event = customer_records['request']['event']

        if event == "customerAgeData":
            # Read customer_data.csv
            df = pd.read_csv(CUSTOMER_DATA)
            ages = []
            for _, row in df.iterrows():
                ages.append(str(row['Age']))

            # Make JSON
            response_json = {
                "request": {
                    "event": "customerAgeData",
                    "body": {
                        "customerAge": ages
                    }
                }
            }

        else:
            response_json = {
                "request": {
                    "event": "customerAgeData",
                    "body": {
                        "customerAge": []
                    }
                }
            }

        # Response JSON data
        socket.send_json(response_json)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    customer_records()
