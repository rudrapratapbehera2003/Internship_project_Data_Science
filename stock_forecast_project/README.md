Stock Forecasting Web Application:
- A Django-based web application that forecasts stock prices using the Facebook Prophet model.
- Developed as part of an internship project focused on time-series forecasting, model deployment, and data-driven insights.

Features:
- Interactive web interface built with Django.
- Forecasts stock prices for user-specified future time periods.
- Visualizes predicted trends using dynamic matplotlib plots.
- Handles data preprocessing and lag-based feature engineering.
- Simple deployment-ready structure with requirements.txt.

Tech Stack:
- Backend: Django (Python)
- Forecasting Model: Prophet
- Libraries: Pandas, NumPy, Matplotlib
- Frontend: HTML, CSS (Django Templates)

Installation:
Clone the repository:(use following commands)
git clone https://github.com/rudrapratapbehera2003/Internship_project_Data_Science.git
cd stock_forecast_project # Open project project folder 


Create a virtual environment
python -m venv venv # Create your virtual enviroment 
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For macOS/Linux


Install dependencies:
pip install -r requirements.txt


Run the server:(use following commands)
cd stock_forecast # go to the main app
python manage.py runserver


Open in browser:
http://127.0.0.1:8000/

Note:
- If you encounter a “script not allowed to run” error on Windows PowerShell, enable scripts using:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  # Use this command

Output Preview
-Displays a forecasted stock trend graph.
-Shows tabular predicted results with key metrics.
-Easy-to-understand and ready for presentation/demo.

Conclusion
- This project demonstrates end-to-end time series forecasting, from data understanding to deployment.
- It combines data science and software engineering skills into a single, deployable solution.