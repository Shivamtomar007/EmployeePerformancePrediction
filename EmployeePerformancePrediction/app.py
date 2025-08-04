from flask import Flask, render_template, request
import pandas as pd
from joblib import load
# import os

app = Flask(__name__)

# Load the trained model
model = load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        data = {
            'targeted_productivity': float(request.form['targeted_productivity']),
            'smv': float(request.form['smv']),
            'over_time': float(request.form['over_time']),
            'incentive': float(request.form['incentive']),
            'no_of_workers': float(request.form['no_of_workers']),
            'department': request.form['department'],
            'day': request.form['day']
        }
        
        # Convert to DataFrame
        df = pd.DataFrame(data, index=[0])
        
        # Make prediction
        prediction = model.predict(df)[0]
        
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)