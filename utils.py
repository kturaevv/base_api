import csv
import datetime
import random
import sys
from uuid import uuid4

import pandas as pd


def _random_timestamp():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    dt = datetime.datetime(2022, 11, 11, hour, minute)
    return datetime.datetime.timestamp(dt)


def fake_data():
    """ Fake data for Pandas dataframe with columns ['customer_id', 'product_id', 'timestamp']"""
    return {
        "customer_id": uuid4(),
        "product_id": random.randint(1, 1000),
        "timestamp": _random_timestamp()
    }


def create_dataframe(n: int):
    df = pd.DataFrame([fake_data() for _ in range(n)])
    return df


def generate_fake_csv():
    with open('fake_data.csv', 'w') as csvfile:
        fieldnames = [*fake_data().keys()]
        print("Fieldnames", fieldnames, end='\n')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(100000):
            writer.writerow(fake_data())
            if i != 0 and i % 1000000 == 0:
                print("1,000,000 rows written...")
                sys.stdout.flush()
