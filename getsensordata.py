import Adafruit_DHT
import yaml
from gpiozero import CPUTemperature
from datetime import datetime

with open("/home/pi/code/climate-sensor/sensor_config.yaml", "r") as cfg:
	config = yaml.load(cfg, Loader=yaml.FullLoader)

SENSOR_LOCATION_NAME = config["SENSOR_LOCATION_NAME"]

humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
cpu_temp = CPUTemperature().temperature
date = datetime.now()
format_args = ["PI TIME", date.strftime("%Y-%m-%d %H:%M:%S"), "SENSOR", SENSOR_LOCATION_NAME, "TEMPERATURE", temp_c,
	       "HUMIDITY", humidity, "CPU TEMPERATURE", cpu_temp]
print("\n{:<20}: {}\n{:<20}: {}\n{:<20}: {:.2f} C\n{:<20}: {:.2f} %\n{:<20}: {:.2f} C\n".format(*format_args))
