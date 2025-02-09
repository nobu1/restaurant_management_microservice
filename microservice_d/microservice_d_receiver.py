import zmq
import pandas as pd


RESTAURANT_DATA = "../csv/restaurants_data.csv"


def restaurant_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:30003")

    print("Restaurant Records Receiver Startup.")

    while True:
        # Receive JSON request
        restaurant_records = socket.recv_json()

        # Confirm event data
        event = restaurant_records['request']['event']

        if event == "restaurantData":
            # Read restaurants_data.csv
            df = pd.read_csv(RESTAURANT_DATA)
            open = 0
            under_renovation = 0
            opening_preparation = 0

            for _, row in df.iterrows():
                if row['Status'] == "Open":
                    open += 1
                elif row['Status'] == "Under Renovation":
                    under_renovation += 1
                elif row['Status'] == "Opening Preparation":
                    opening_preparation += 1

            # Make JSON
            response_json = {
                "request": {
                    "event": "restaurantData",
                    "body": {
                        "Open": open,
                        "Under Renovation": under_renovation,
                        "Opening Preparation": opening_preparation
                    }
                }
            }

        else:
            response_json = {
                "request": {
                    "event": "restaurantData",
                    "body": {
                        "Open": 0,
                        "Under Renovation": 0,
                        "Opening Preparation": 0
                    }
                }
            }

        # Response JSON data
        socket.send_json(response_json)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    restaurant_records()
