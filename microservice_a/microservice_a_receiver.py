import zmq
import pandas as pd


RESERVATION_DATA = "../csv/reservation_data.csv"


def reservaion_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:30000")

    print("Reservation Records Receiver Startup.")

    while True:
        reservation_records = socket.recv_json()

        # Request message validation
        event = reservation_records['request']['event']
        if event == "reservationData":
            # Extract customer name from JSON
            customer_name = \
                reservation_records['request']['body']['customerName']

            # Extract customer data from customer_data.csv
            df = pd.read_csv(RESERVATION_DATA)
            df = df[df['Name'] == customer_name]

            # Initialize JSON
            response_json = {
                "request": {
                    "event": "reservationData",
                    "body": {
                        "customerName": customer_name,
                        "history": []
                    }
                }
            }

            # Append histories data
            for _, row in df.iterrows():
                response_json["request"]["body"]["history"].append({
                    "Date": str(row['Date']),
                    "Time": str(row['Time']),
                    "Number": str(row['Number'])
                })

        else:
            response_json = {
                "request": {
                    "event": "reservationData",
                    "body": {
                        "customerName": customer_name,
                        "history": []
                    }
                }
            }

        socket.send_json(response_json)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    reservaion_records()
