import zmq
import pandas as pd
from datetime import datetime as dt


COUPONS_DATA = "../csv/coupons_data.csv"
CONNECTION_PORT = 30002


def response_json_with_coupon_data(socket, price, percent):
    # Construct JSON
    response_json = {
        "response": {
            "event": "couponData",
            "body": {
                "Percent": percent,
                "Price": price
            }
        }
    }
    print(f"Response sent was: {response_json}")
    socket.send_json(response_json)


def coupon_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + str(CONNECTION_PORT))

    print("Coupons Records Receiver Startup.")

    while True:
        # Set variables
        coupon_records = socket.recv_json()
        event = coupon_records['request']['event']
        percent = price = 0

        # Confirm event data
        if event == "couponData":
            # Extract start and end period and convert to datatime
            start = dt.strptime(
                coupon_records['request']['body']['startPeriod'],
                '%Y-%m-%d'
            )
            end = dt.strptime(
                coupon_records['request']['body']['endPeriod'],
                '%Y-%m-%d'
            )

            df = pd.read_csv(COUPONS_DATA)

            # Collect percent and price data with specified period
            for _, row in df.iterrows():
                if start <= pd.to_datetime(row['ValidDate']) <= end:
                    if row['Type'] == "Percent":
                        percent += 1
                    elif row['Type'] == "Price":
                        price += 1

            response_json_with_coupon_data(socket, price, percent)
        else:
            response_json_with_coupon_data(socket, price, percent)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    coupon_records()
