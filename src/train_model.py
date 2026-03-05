import pandas as pd
import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# load dataset
df = pd.read_csv("../dataset/processed_features.csv")

# features and target
X = df[[
    "hour",
    "day_of_week",
    "weekend",
    "duration_hours"
]]

y = df["available_spots"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------
# Linear Regression
# ------------------------

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# ------------------------
# Random Forest
# ------------------------

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# save models
os.makedirs("../models", exist_ok=True)

with open("../models/linear_model.pkl", "wb") as f:
    pickle.dump(linear_model, f)

with open("../models/random_forest.pkl", "wb") as f:
    pickle.dump(rf_model, f)

print("Models trained successfully!")
print("Models saved in /models folder")