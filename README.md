# 🚗 Smart Parking Prediction System

An AI-based Smart Parking Management System that predicts the number of available parking spots using Machine Learning.  
The system helps improve parking efficiency by estimating availability and displaying the status through a web dashboard.

---

## 📌 Project Overview

Parking congestion is a common issue in malls, offices, and public areas.  
This project uses Machine Learning to predict the number of available parking spots based on parking usage data.

The system provides a simple dashboard where users can click **Predict** to view:

- Available parking spots
- Parking status (Available / Almost Full)
- Visual progress indicator

---

## ⚙️ Technologies Used

- **Python**
- **Flask**
- **Machine Learning (Scikit-learn)**
- **Random Forest Regression**
- **HTML**
- **CSS**
- **JavaScript**

---

## 🧠 Machine Learning Models Used

Two models were tested:

### Linear Regression
MAE: 12.19  
RMSE: 15.11  
R² Score: 0.15  

### Random Forest
MAE: 0.014  
RMSE: 0.081  
R² Score: 0.9999  

Random Forest performed significantly better and was used for prediction.

---

## 🖥️ Features

- Predict parking availability
- Dashboard showing parking statistics
- Parking status indicator
- Progress bar visualization
- Simple and responsive UI

---

## ▶️ How to Run the Project

1️⃣ Clone the repository

2️⃣ Go to project folder

3️⃣ Install dependencies

4️⃣ Run the Flask application

5️⃣ Open browser and go to http://127.0.0.1:5000


---

## 📊 Future Improvements

- Real-time parking sensor integration
- Live parking visualization grid
- Mobile application integration
- AI model optimization with larger datasets
- Support for small parking areas (research gap improvement)

---

## 🎯 Research Gap Addressed

Many smart parking systems assume large smart-city infrastructure.  
This project focuses on **small-scale parking environments** and demonstrates how AI prediction can still be applied effectively.

---

## 👨‍💻 Author

Aditya Patil
