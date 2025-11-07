from django.shortcuts import render
import os
from io import BytesIO
import base64
import numpy as np
import pandas as pd
from datetime import timedelta
import pickle
import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt
from django.conf import settings



NASDAQ_MODEL_PATH = os.path.join(settings.BASE_DIR, "models", "prophet_model_nasdaq.pkl")
STOCK_MODEL_PATH = os.path.join(settings.BASE_DIR, "models", "prophet_stock_model.pkl")

with open(NASDAQ_MODEL_PATH, "rb") as f:
    model_nasdaq = pickle.load(f)

with open(STOCK_MODEL_PATH, "rb") as f:
    model_stock = pickle.load(f)



def generate_trading_hours(start_dt, steps, start_hour=3, end_hour=20):
    out = []
    cur = pd.Timestamp(start_dt)
    while len(out) < steps:
        cur = cur + timedelta(hours=1)
        if cur.weekday() >= 5: 
            days_to_monday = 7 - cur.weekday()
            cur = (cur + timedelta(days=days_to_monday)).replace(hour=start_hour, minute=0, second=0)
            continue
        if cur.hour < start_hour:
            cur = cur.replace(hour=start_hour)
        elif cur.hour > end_hour:
            cur = (cur + timedelta(days=1)).replace(hour=start_hour)
            continue
        if start_hour <= cur.hour <= end_hour:
            out.append(pd.Timestamp(cur))
    return pd.DataFrame({"ds": out})


def forecast_nasdaq_for_ds(ds_df):
    preds = model_nasdaq.predict(ds_df)
    return pd.DataFrame({"ds": ds_df["ds"], "nasdaq_index_pred": preds["yhat"]})



def forecast_stock_iterative(model_stock, history_df, nasdaq_future_df, periods):
    history = history_df.copy().reset_index(drop=True)
    preds = []
    nasdaq_future_df = nasdaq_future_df.reset_index(drop=True)

    for t in range(periods):
        next_ds = nasdaq_future_df.loc[t, "ds"]
        nasdaq_val = nasdaq_future_df.loc[t, "nasdaq_index_pred"]

        row = {"ds": next_ds, "nasdaq_index": nasdaq_val}
        for i in range(1, 5):
            row[f"lag_{i}"] = history["y"].iloc[-i]

        next_df = pd.DataFrame([row])
        next_df = next_df.bfill().ffill() 

        yhat = model_stock.predict(next_df)["yhat"].iloc[0]
        row["y"] = yhat

        preds.append(row)
        history = pd.concat([history, pd.DataFrame([row])], ignore_index=True)

    return pd.DataFrame(preds)


def forecast_view(request):
    forecast_table = None
    plot_base64 = None

    if request.method == "POST":
        try:
            periods = int(request.POST.get("days", 0))
            if periods <= 0:
                raise ValueError
        except Exception:
            periods = 30

        history = model_stock.history.copy().sort_values("ds").reset_index(drop=True)
        last_ds = history["ds"].max()

      
        future_ds_df = generate_trading_hours(last_ds, periods)

     
        nasdaq_future = forecast_nasdaq_for_ds(future_ds_df)

     
        stock_preds = forecast_stock_iterative(model_stock, history, nasdaq_future, periods)

        forecast_table = stock_preds[["ds", "y", "nasdaq_index", "lag_1", "lag_2", "lag_3", "lag_4"]]
        forecast_table.rename(columns={"y": "predicted_stock"}, inplace=True)
        forecast_table["ds"] = forecast_table["ds"].dt.strftime("%Y-%m-%d %H:%M:%S")

        plt.figure(figsize=(12, 5))
        hist_plot = history[["ds", "y"]].tail(120)
        plt.plot(hist_plot["ds"], hist_plot["y"], label="Historical", color="orange")
        plt.plot(stock_preds["ds"], stock_preds["y"], label="Forecast", color="green", marker="o")
        plt.xticks(rotation=45)
        plt.title(f"Stock Forecast for Next {periods} Trading Hours")
        plt.legend()
        plt.tight_layout()

 
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        buffer.close()
        plot_base64 = f"data:image/png;base64,{image_base64}"
        plt.close()

    forecast_records = forecast_table.to_dict(orient="records") if forecast_table is not None else None

    return render(request, "predictor/forecast.html", {
        "forecast_table": forecast_records,
        "plot_base64": plot_base64,
    })
