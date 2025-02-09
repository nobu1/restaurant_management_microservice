import zmq
import pandas as pd
from datetime import datetime as dt


COUPONS_DATA = "../csv/coupons_data.csv"


def coupon_records():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:30002")

    print("Coupons Records Receiver Startup.")

    while True:
        # Receive JSON request
        coupon_records = socket.recv_json()

        # Confirm event data
        event = coupon_records['request']['event']

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

            # Read coupon_data.csv
            df = pd.read_csv(COUPONS_DATA)
            percent = 0
            price = 0
            for _, row in df.iterrows():
                if start <= pd.to_datetime(row['ValidDate']) <= end:
                    if row['Type'] == "Percent":
                        percent += 1
                    elif row['Type'] == "Price":
                        price += 1

            # Make JSON
            response_json = {
                "request": {
                    "event": "couponData",
                    "body": {
                        "Percent": percent,
                        "Price": price
                    }
                }
            }

        else:
            response_json = {
                "request": {
                    "event": "couponData",
                    "body": {
                        "Percent": 0,
                        "Price": 0
                    }
                }
            }

        # Response JSON data
        socket.send_json(response_json)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    coupon_records()
