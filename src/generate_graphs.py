import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("dataset/raw_parking_logs.csv")

df["entry_time"] = pd.to_datetime(df["entry_time"])

df["hour"] = df["entry_time"].dt.hour

hourly_counts = df.groupby("hour").size()

plt.figure()

hourly_counts.plot(kind="bar")

plt.title("Parking Demand by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Vehicles")

os.makedirs("static", exist_ok=True)

plt.savefig("static/hourly_demand.png")

print("Graph generated")