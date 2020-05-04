import Adafruit_DHT
import yaml

with open("sensor_config.yaml", "r") as cfg:
	config = yaml.load(cfg, Loader=yaml.FullLoader)

SENSOR_LOCATION_NAME = config["SENSOR_LOCATION_NAME"]

humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
format_args = ["SENSOR", SENSOR_LOCATION_NAME, "TEMPERATURE", temp_c,
	       "HUMIDITY", humidity]
print("\n{:<20}: {}\n{:<20}: {:.2f} C\n{:<20}: {:.2f} %\n".format(*format_args))
