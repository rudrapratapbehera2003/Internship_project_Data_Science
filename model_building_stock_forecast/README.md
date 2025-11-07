Stock Price Forecasting – Model Development:
- This folder contains the complete model building workflow for stock price forecasting.
- It includes all stages — from data understanding and preprocessing to model evaluation and selection.
- The project focuses on analyzing multiple forecasting techniques and finalizing the most accurate one for deployment.

Project Workflow
1. Data Understanding
- Collected historical stock price data and relevant market indices.
- Observed long-term upward trends with short-term volatility.
- Identified seasonal patterns (notably during Q3–Q4).

2. Data Preprocessing
- Handled missing values using forward-fill methods.
- Converted Date column to datetime format and set as index.
- Removed anomalies and ensured time-based ordering for modeling.

3. Dataset Preparation
- Two datasets were created for flexibility across models:
- Dataset 1: Without lagged features — used for models that handle lag internally.
- Dataset 2: With lagged features (t-1, t-2, …) — used for models requiring explicit temporal dependencies.

4. Statistical Analysis
- Applied Augmented Dickey-Fuller (ADF) test for stationarity checks.
- Used ACF and PACF plots to identify AR and MA components for ARIMA/SARIMA modeling.

5. Model Building
- Evaluated multiple forecasting approaches:
- ARIMA / SARIMA: For baseline statistical forecasting.
- Ensemble Models (Random Forest, XGBoost, LightGBM): To capture non-linear trends.
- Prophet Model: For trend-seasonality decomposition and robust forecasting.
- LSTM: For capturing sequential dependencies in time series data.
- Each model(Those do not handle lags internally) was trained and evaluated using both dataset versions (with and without lags).

6. Model Selection
- Models were compared based on RMSE, MAE, and visual fit with actual data.
- The Prophet model with lag-based regressors achieved the best balance between accuracy and generalization.

Tools & Libraries
- Python, Pandas, NumPy, Matplotlib, Seaborn
- Statsmodels (ARIMA, ACF, PACF)
- Scikit-learn (train-test splits, evaluation metrics)
- XGBoost, LightGBM, RandomForestRegressor
- Prophet
- TensorFlow / Keras (for LSTM)

Outcome:
- Built, tested, and compared multiple forecasting models.
- Identified Prophet (with lagged regressors) as the most reliable model.
- Prepared final .pkl models for integration into Django-based deployment.

Conclusion:
This folder captures the core data science process — from EDA to model optimization and evaluation — forming the foundation for the final deployed forecasting application.