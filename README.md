End-to-End Stock Price Forecasting Project:
- This repository presents a complete end-to-end stock forecasting system developed as part of an internship project.
- The project covers every major stage of the data science workflow — from data collection and preprocessing to model development, evaluation, and web deployment using Django.

Project Overview:
- The goal of this project is to forecast stock prices using historical data and market indices (like NASDAQ) through various machine learning and time-series models.
- It also includes a fully functional Django web application that allows real-time prediction and visualization of future stock movements using the final deployed model.

Project Phases:
1. Data Understanding & Preprocessing
- Collected and analyzed historical stock data.
- Detected long-term upward trends and short-term volatility.
- Cleaned and formatted data: handled missing values, converted date columns, and prepared time-indexed datasets.
- Created two datasets — one with lag features and one without lag features — to suit different model requirements.

2. Model Building & Evaluation
- Built and compared several forecasting models:
- Statistical Models: ARIMA, SARIMA
- Ensemble Models: Random Forest, XGBoost, LightGBM
- Advanced Models: Prophet, LSTM
- Evaluated each model on metrics like RMSE, MAE, and trend alignment.
- Prophet model (enhanced with lag and NASDAQ regressors) achieved the best results, showing stable and realistic forecasts.
- All trained models were exported as .pkl files for integration.
(Detailed model analysis is available inside the model_building/ folder.)

3. Model Deployment (Django Application):
- Integrated the final Prophet model into a Django web application.
- Built a clean user interface to input future time periods and visualize forecasts.
- The system dynamically generates future timestamps, forecasts NASDAQ trends, and predicts stock prices iteratively.
- Forecast plots and tabular predictions are rendered directly on the web interface.
(Deployment details and setup instructions are available inside the stock_forecast_project/ folder.)

Installation:
Clone the repository:(use following commands)
git clone https://github.com/rudrapratapbehera2003/Internship_project_Data_Science.git