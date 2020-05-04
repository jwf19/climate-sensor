import Adafruit_DHT
from ISStreamer.Streamer import Streamer
import time
import yaml


# ------- User Settings ---------
with open("sensor_config.yaml", "r") as cfg:
	config  = yaml.load(cfg, loader=yaml.FullLoader)

SENSOR_LOCATION_NAME = config["SENSOR_LOCATION_NAME"]
BUCKET_NAME = config["BUCKET_NAME"]
BUCKET_KEY = config["BUCKET_KEY"]
ACCESS_KEY = config["ACCESS_KEY"]
MINUTES_BETWEEN_READS = config["MINUTES_BETWEEN_READS"]
METRIC_UNITS = config["METRIC_UNITS"]
# -------------------------------

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
while True:
	humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
	if METRIC_UNITS:
		streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", format(temp_c, ".2f"))
		print("{} Temperature {:.2f} C".format(SENSOR_LOCATION_NAME, temp_c))
	else:
		temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")
		streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
	humidity = format(humidity, ".2f")
	streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
	print("{} Humidity {} %".format(SENSOR_LOCATION_NAME, humidity))
	streamer.flush()
	time.sleep(60.0 * MINUTES_BETWEEN_READS)

