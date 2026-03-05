import pandas as pd
import random
from datetime import datetime, timedelta
import os

# configuration
TOTAL_SPOTS = 50
DAYS = 30
RECORDS = 4000

data = []

start_date = datetime(2025, 1, 1)

for i in range(RECORDS):

    # random day
    random_day = start_date + timedelta(days=random.randint(0, DAYS-1))

    # peak hour bias
    peak_hours = list(range(10,14)) + list(range(17,21))

    if random.random() < 0.6:
        hour = random.choice(peak_hours)
    else:
        hour = random.randint(0,23)

    minute = random.randint(0,59)

    entry_time = random_day.replace(hour=hour, minute=minute)

    # parking duration
    duration_hours = random.randint(1,3)

    exit_time = entry_time + timedelta(hours=duration_hours)

    spot_no = random.randint(1, TOTAL_SPOTS)

    data.append([
        i+1,
        spot_no,
        entry_time,
        exit_time,
        duration_hours
    ])

df = pd.DataFrame(data, columns=[
    "log_id",
    "spot_no",
    "entry_time",
    "exit_time",
    "duration_hours"
])

# ensure dataset folder exists
os.makedirs("../dataset", exist_ok=True)

df.to_csv("../dataset/raw_parking_logs.csv", index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))