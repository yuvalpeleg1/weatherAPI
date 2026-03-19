from flask import Flask, request, render_template
import requests
from myKey import getAPI

app = Flask(__name__)

API_KEY = getAPI()


@app.route("/", methods=["GET", "POST"])
def home():
    temp = None
    date = None

    if request.method == "POST":
        date = request.form["date"]
        API_URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/tel%20aviv/{date}"
        PARAMS = {
            "unitGroup": "metric",
            "include": "days",
            "key": API_KEY,
            "contentType": "json",
        }

        res = requests.get(API_URL, params=PARAMS)
        data = res.json()

        temp = data["days"][0]["temp"]
    return render_template("index.html", temp=temp, date=date)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
