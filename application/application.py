from flask import Flask, render_template
import Adafruit_DHT
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def read_sensor():
    sensor_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    humidity = f"{humidity:0.2f}"
    temp_c = f"{temp_c:0.2f}"
    return render_template("sensor_reading.html", humidity=humidity, temperature=temp_c, sensor_datetime=sensor_datetime)


@app.route("/hello-world")
def hello_world():
    return render_template("home.html", thing_to_say="Hello, World!")
