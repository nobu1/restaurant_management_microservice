import zmq
import pandas as pd


CUSTOMER_DATA = "../csv/customers_data.csv"
CONNECTION_PORT = 30001


def response_json_with_customer_age(socket, ages):
    # Construct JSON
    response_json = {
        "response": {
            "event": "customerAgeData",
            "body": {
                "customerAge": ages
            }
        }
    }
    socket.send_json(response_json)


def customer_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + str(CONNECTION_PORT))

    print("Customer Records Receiver Startup.")

    while True:
        # Set variables
        customer_records = socket.recv_json()
        event = customer_records['request']['event']
        ages = []

        # Confirm event data
        if event == "customerAgeData":
            df = pd.read_csv(CUSTOMER_DATA)

            # Collect customer ages
            for _, row in df.iterrows():
                ages.append(str(row['Age']))

            response_json_with_customer_age(socket, ages)
        else:
            response_json_with_customer_age(socket, ages)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    customer_records()
