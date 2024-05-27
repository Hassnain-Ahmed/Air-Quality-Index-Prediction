from flask import Flask, render_template
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


def loadData():

    csvData = pd.read_csv("static/Dataset/AirQualityUCI.csv")
    csvData = pd.read_csv("static/Dataset/AirQualityUCI.csv", sep=";", decimal=",")
    csvData = csvData.iloc[:, :-2]
    csvData = csvData.head(9357)
    csvData = csvData.replace(to_replace=-200, value=np.NaN)
    csvData = csvData.fillna(csvData.mean(numeric_only="None"))

    dateInfo = pd.to_datetime(csvData["Date"], format="mixed")

    timeInfo = csvData["Time"].apply(lambda x: x.replace(".", ":"))

    dateTime = pd.concat([dateInfo, timeInfo], axis=1)

    dateTime["ds"] = dateTime["Date"].astype(str) + " " + dateTime["Time"].astype(str)

    data = pd.DataFrame()
    data["ds"] = pd.to_datetime(dateTime["ds"])

    return data, csvData


def graphRH(data, csvData, filename):
    model = Prophet()
    data["y"] = csvData["RH"]

    model.fit(data)
    future = model.make_future_dataframe(periods=365, freq="H")
    forecast = model.predict(future)
    pred_info = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].mean()
    graph_RH = model.plot(forecast)

    fig_path = os.path.join("static", "graphs", filename)
    graph_RH.savefig(fig_path)
    plt.close(graph_RH)

    return fig_path, pred_info


def graphAH(data, csvData, filename):
    model = Prophet()
    data["y"] = csvData["AH"]

    model.fit(data)
    future = model.make_future_dataframe(periods=365, freq="H")
    forecast = model.predict(future)
    pred_info = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].mean()
    graph_AH = model.plot(forecast)

    fig_path = os.path.join("static", "graphs", filename)
    graph_AH.savefig(fig_path)
    plt.close(graph_AH)

    return fig_path, pred_info


def graphT(data, csvData, filename):
    model = Prophet()
    data["y"] = csvData["T"]

    model.fit(data)
    future = model.make_future_dataframe(periods=365, freq="H")
    forecast = model.predict(future)
    pred_info = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].mean()
    graph_T = model.plot(forecast)

    fig_path = os.path.join("static", "graphs", filename)
    graph_T.savefig(fig_path)
    plt.close(graph_T)

    return fig_path, pred_info


@app.route("/")
def home():
    data, csvData = loadData()
    graph_t, pred_mean_t = graphT(data, csvData, "T.png")
    graph_ah, pred_mean_ah = graphAH(data, csvData, "AH.png")
    graph_rh, pred_mean_rh = graphRH(data, csvData, "RH.png")

    return render_template(
        "index.html",
        graph_ah=graph_ah,
        graph_t=graph_t,
        graph_rh=graph_rh,
        pred_mean_t=pred_mean_t,
        pred_mean_ah=pred_mean_ah,
        pred_mean_rh=pred_mean_rh,
    )


@app.route("/temprature")
def temprature():
    return render_template("Table.html")


if __name__ == "__main__":
    app.run(debug=True)
