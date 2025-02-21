import zmq
import pandas as pd


RESTAURANT_DATA = "../csv/restaurants_data.csv"
CONNECTION_PORT = 30003


def response_json_with_restaurant_status(socket, restaurant_status):
    # Construct JSON
    response_json = {
        "response": {
            "event": "restaurantData",
            "body": {
                "Open": restaurant_status["open"],
                "Under Renovation": restaurant_status["under_renovation"],
                "Opening Preparation": restaurant_status["opening_preparation"]
            }
        }
    }
    socket.send_json(response_json)


def restaurant_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + str(CONNECTION_PORT))

    print("Restaurant Records Receiver Startup.")

    while True:
        # Set variables
        restaurant_records = socket.recv_json()
        event = restaurant_records['request']['event']
        restaurant_status = {
            "open": 0,
            "under_renovation": 0,
            "opening_preparation": 0
        }

        # Confirm event data
        if event == "restaurantData":
            df = pd.read_csv(RESTAURANT_DATA)

            # Collect restaurant status data
            for _, row in df.iterrows():
                if row['Status'] == "Open":
                    restaurant_status["open"] += 1
                elif row['Status'] == "Under Renovation":
                    restaurant_status["under_renovation"] += 1
                elif row['Status'] == "Opening Preparation":
                    restaurant_status["opening_preparation"] += 1

            response_json_with_restaurant_status(socket, restaurant_status)
        else:
            response_json_with_restaurant_status(socket, restaurant_status)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    restaurant_records()
