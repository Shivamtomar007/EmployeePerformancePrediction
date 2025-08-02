

---

````markdown
# 🌟 Employee Performance Prediction

The project analyzes employee data and builds a predictive model to help organizations identify high-performing employees and make data-driven HR decisions.

---

## 📌 Overview
This project predicts employee performance using machine learning and serves predictions through a simple web application built with **Flask**.  
It combines data preprocessing, model training, and a web interface to make predictions user-friendly and interactive.

### **The goal:**
- ✅ Help organizations make data-driven HR decisions
- ✅ Identify high-performing employees based on historical data
- ✅ Provide quick predictions via a web interface

---

## 📊 Dataset
Dataset used:  
🔗 [Productivity Prediction of Garment Employees (Kaggle)](https://www.kaggle.com/datasets/utkarshsarbahi/productivity-prediction-of-garment-employees)

**Includes:**
- Department, day, team, targeted productivity
- Actual productivity
- Factors like work hours, breaks, etc.

**Data preprocessing handles:**
- Missing values
- Encoding categorical data
- Scaling numerical features

---

## ✨ Features
- ✅ Data cleaning and preprocessing
- ✅ Exploratory Data Analysis (EDA) notebook
- ✅ Machine learning model training & saving (`model.joblib`)
- ✅ Flask web app (`app.py`) with:
  - HTML templates for input & results
  - CSS styling
- ✅ Modular Python scripts (`src/`)

---

## 📁 Project Structure
```text
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
├── requirements.txt
└── README.md
````

---

## 🚀 Getting Started

**1️⃣ Clone the repository**

```bash
git clone "ur"
```

**2️⃣ (Optional) Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Train the model (if needed)**

```bash
python src/train_model.py
```

**5️⃣ Run the web app**

```bash
python app.py
```

Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Screenshots

*Add screenshots here after adding them to your project (e.g., `images/app_screenshot.png`):*

```markdown
![Web App UI](images/app_screenshot.png)
```

---

## 📜 Requirements

* Python 3.9+
* Flask
* pandas
* scikit-learn
* matplotlib, seaborn
  (see `requirements.txt` for full list)

---

## 🤝 Contributing

Contributions and suggestions are welcome!

* Fork the repository
* Open an issue
* Submit a pull request

```
