import pandas as pd
import pickle
import matplotlib.pyplot as plt
import os

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# load dataset
df = pd.read_csv("./dataset/processed_features.csv")

X = df[[
    "hour",
    "day_of_week",
    "weekend",
    "duration_hours"
]]

y = df["available_spots"]

# split again for evaluation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# load models
with open("./models/linear_model.pkl", "rb") as f:
    linear_model = pickle.load(f)

with open("./models/random_forest.pkl", "rb") as f:
    rf_model = pickle.load(f)

# predictions
linear_pred = linear_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

# metrics
linear_mae = mean_absolute_error(y_test, linear_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)

linear_rmse = np.sqrt(mean_squared_error(y_test, linear_pred))
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

linear_r2 = r2_score(y_test, linear_pred)
rf_r2 = r2_score(y_test, rf_pred)

print("\nModel Evaluation Results\n")

print("Linear Regression")
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R2:", linear_r2)

print("\nRandom Forest")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
print("R2:", rf_r2)


plt.figure()

plt.scatter(y_test, rf_pred)

plt.xlabel("Actual Available Spots")
plt.ylabel("Predicted Available Spots")

plt.title("Actual vs Predicted Parking Availability")

plt.savefig("./visualization/prediction_accuracy.png")

plt.show()


# graph comparison
models = ["Linear Regression", "Random Forest"]
mae_scores = [linear_mae, rf_mae]

plt.bar(models, mae_scores)
plt.title("Model Comparison (MAE)")
plt.ylabel("Error")

os.makedirs("./visualization", exist_ok=True)

plt.savefig("./visualization/model_comparison.png")
plt.show()