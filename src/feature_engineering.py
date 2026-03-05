import pandas as pd
import os

TOTAL_SPOTS = 50

# load dataset
df = pd.read_csv("../dataset/raw_parking_logs.csv")

# convert time columns
df["entry_time"] = pd.to_datetime(df["entry_time"])
df["exit_time"] = pd.to_datetime(df["exit_time"])

# extract time features
df["hour"] = df["entry_time"].dt.hour
df["day_of_week"] = df["entry_time"].dt.dayofweek

# weekend flag
df["weekend"] = df["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

# vehicles entering per hour
hourly_traffic = df.groupby(["day_of_week","hour"]).size().reset_index(name="vehicles_this_hour")

df = pd.merge(df, hourly_traffic, on=["day_of_week","hour"], how="left")

# calculate available spots
df["available_spots"] = TOTAL_SPOTS - df["vehicles_this_hour"]

# prevent negative values
df["available_spots"] = df["available_spots"].apply(lambda x: max(x,0))

# keep only ML features
features = df[[
    "hour",
    "day_of_week",
    "weekend",
    "duration_hours",
    "available_spots"
]]

# save processed dataset
os.makedirs("../dataset", exist_ok=True)

features.to_csv("../dataset/processed_features.csv", index=False)

print("Feature engineering complete!")
print("Saved to dataset/processed_features.csv")