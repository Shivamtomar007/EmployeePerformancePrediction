import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from joblib import dump
import os

# Selected columns based on EDA
SELECTED_FEATURES = [
    'targeted_productivity',
    'smv',
    'over_time',
    'incentive',
    'no_of_workers',
    'department',
    'day'
]
TARGET = 'actual_productivity'

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '../data/garments_worker_productivity.csv')
    df = pd.read_csv(data_path)
    
    # Select only useful columns
    df = df[SELECTED_FEATURES + [TARGET]]
    
    return df

def preprocess_data(df):
    # Define feature types
    cat_features = ['department', 'day']
    num_features = [col for col in SELECTED_FEATURES if col not in cat_features]
    
    X = df[SELECTED_FEATURES]
    y = df[TARGET]
    
    return X, y, cat_features, num_features

def train_model():
    df = load_data()
    X, y, cat_features, num_features = preprocess_data(df)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    # Preprocessing pipelines
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_features),
            ('cat', categorical_transformer, cat_features)])
    
    # Model pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])
    
    # Train and evaluate
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print(f"RMSE: {mean_squared_error(y_test, y_pred)**0.5:.4f}")
    print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")
    
    # Save model
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '../model.joblib')
    dump(model, model_path)
    print(f"Model saved as {model_path}")

if __name__ == "__main__":
    train_model()