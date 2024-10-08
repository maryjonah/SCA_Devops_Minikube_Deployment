from flask import Flask, render_template
from opentelemetry import trace
import requests

app = Flask(__name__)
tracer = trace.get_tracer(__name__)

API_URL = "https://zenquotes.io/api/today"


@app.route("/")
def index():
    with tracer.start_as_current_span("zenquotes_for_today") as span:
        quote_of_day_data = requests.get(API_URL).json()
        quote = quote_of_day_data[0]["q"]
        return render_template("index.html", quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
