# EmployeePerformancePrediction
The project analyzes employee data and builds a predictive model to help organizations identify high-performing employees and make data-driven HR decisions.
📌 Overview
This project predicts employee performance using machine learning and serves predictions through a simple web application built with Flask.
It combines data preprocessing, model training, and a web UI to make predictions user-friendly and interactive.

The goal:
✅ Help organizations make data-driven HR decisions
✅ Identify high-performing employees based on historical data
✅ Provide quick predictions via a web interface
📊 Dataset
The dataset used link: https://www.kaggle.com/datasets/utkarshsarbahi/productivity-prediction-of-garment-employees
Includes:
Department, day, team, and targeted productivity
Actual productivity
Factors like work hours, breaks, and more
Data preprocessing handles:
Missing values
Encoding categorical data
Scaling numerical features
✨ Features
✅ Data cleaning and preprocessing
✅ Exploratory Data Analysis (EDA) notebook
✅ Machine learning model training & saving (model.joblib)
✅ Flask web app (app.py) with:
HTML templates for input & results
CSS styling
✅ Modular Python scripts (src/)
📁 Project Structure
EMPLOYEEPERFORMANCEPREDICTION/
├── .venv/                    # Virtual environment
├── data/
│   └── garments_worker_productivity.csv
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── train_model.py
│   └── utils.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py                    # Flask web application
├── model.joblib              # Trained ML model
└── requirements.txt          # Python dependencies

🚀 Getting Started
1️⃣ Clone the repository
2️⃣Install dependencies
pip install -r requirements.txt
3️⃣ Train the model
python src/train_model.py
4️⃣ Run the web app
python app.py

🤝 Contributing
Contributions, suggestions, and feature requests are welcome!
Feel free to:
Fork the repo
Open issues
Submit pull requests




