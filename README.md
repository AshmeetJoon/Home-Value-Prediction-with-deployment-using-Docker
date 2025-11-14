# Home-Value-Prediction-with-deployment-using-Docker

A machine learning project to predict home values using an XGBoost model trained on the California Housing dataset. This project demonstrates data preprocessing, model training, hyperparameter tuning, and model deployment using Docker.

## Description

This project uses the California Housing dataset from scikit-learn to build a regression model that predicts median house values in California districts. The workflow includes:

- Data loading and exploration
- Feature scaling using StandardScaler
- Baseline XGBoost model training
- Hyperparameter tuning with GridSearchCV
- Feature importance analysis
- Model saving and loading using joblib

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- joblib

Install the required packages using:
```
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib
```

## Usage

1. Open the `main1.ipynb` notebook in Jupyter Notebook or JupyterLab.
2. Run the cells sequentially to execute the entire pipeline.
3. The trained model will be saved as `xgb_california_model.pkl`.

## Model Details

- **Algorithm**: XGBoost Regressor
- **Hyperparameters Tuned**: n_estimators, max_depth, learning_rate, subsample, colsample_bytree
- **Evaluation Metrics**: Mean Squared Error (MSE), R² Score
- **Feature Importance**: Visualized using seaborn barplot

The model achieves optimal performance through grid search cross-validation.

## Deployment

Containerized with Docker for easy deployment and testing.

Author - Ashmeet Joon
