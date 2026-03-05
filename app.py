from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load trained model
with open("models/random_forest.pkl", "rb") as f:
    model = pickle.load(f)

TOTAL_SPOTS = 50

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    hour = int(request.form["hour"])
    day = int(request.form["day"])
    weekend = int(request.form["weekend"])
    duration = int(request.form["duration"])

    features = np.array([[hour, day, weekend, duration]])

    prediction = model.predict(features)[0]

    prediction = int(round(prediction))

    if prediction > 30:
        status = "Low Occupancy"
    elif prediction > 10:
        status = "Medium Occupancy"
    else:
        status = "Parking Almost Full"

    return render_template(
        "index.html",
        prediction=prediction,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)