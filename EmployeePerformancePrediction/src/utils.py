# import pandas as pd
# import numpy as np
# import joblib
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# # from xgboost import XGBRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline

# def train_models(X: pd.DataFrame, y: pd.Series) -> dict:
#     """
#     Train multiple regression models and return their performance metrics
#     """
#     # Define preprocessing
#     numeric_features = ['targeted_productivity', 'smv', 'over_time', 'incentive', 'no_of_workers']
#     categorical_features = ['department', 'day']
    
#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('num', StandardScaler(), numeric_features),
#             ('cat', OneHotEncoder(), categorical_features)
#         ])
    
#     # Initialize models
#     models = {
#         'LinearRegression': Pipeline([
#             ('preprocessor', preprocessor),
#             ('regressor', LinearRegression())
#         ]),
#         'RandomForest': Pipeline([
#             ('preprocessor', preprocessor),
#             ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
#         ]),
#         'XGBoost': Pipeline([
#             ('preprocessor', preprocessor),
#             ('regressor', XGBRegressor(random_state=42))
#         ])
#     }
    
#     # Split data
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#     # Train and evaluate
#     results = {}
#     for name, model in models.items():
#         model.fit(X_train, y_train)
#         y_pred = model.predict(X_test)
        
#         results[name] = {
#             'model': model,
#             'metrics': {
#                 'MAE': mean_absolute_error(y_test, y_pred),
#                 'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
#                 'R2': r2_score(y_test, y_pred)
#             }
#         }
    
#     return results

# def select_best_model(results: dict) -> tuple:
#     """Select model with best R2 score"""
#     best_model_name = max(results, key=lambda x: results[x]['metrics']['R2'])
#     return best_model_name, results[best_model_name]['model']

# def save_model(model, path: str):
#     """Save trained model to disk"""
#     joblib.dump(model, path)

# def load_model(path: str):
#     """Load saved model from disk"""
#     return joblib.load(path)