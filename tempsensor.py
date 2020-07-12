import Adafruit_DHT
import time
from datetime import datetime
import yaml
from gpiozero import CPUTemperature


# ------- User Settings ---------
with open("/home/pi/code/climate-sensor/sensor_config.yaml", "r") as cfg:
    config = yaml.load(cfg, Loader=yaml.FullLoader)

SENSOR_LOCATION_NAME = config["SENSOR_LOCATION_NAME"]
BUCKET_NAME = config["BUCKET_NAME"]
BUCKET_KEY = config["BUCKET_KEY"]
ACCESS_KEY = config["ACCESS_KEY"]
MINUTES_BETWEEN_READS = config["MINUTES_BETWEEN_READS"]
METRIC_UNITS = config["METRIC_UNITS"]
CSV_FILE = "/home/pi/code/climate-sensor/sensor_readings.csv"
# -------------------------------

while True:
    data_row = []
    sys_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu_temp = CPUTemperature().temperature
    print("\n{} System Time {}".format(SENSOR_LOCATION_NAME, sys_time))
    print("{} CPU Temperature {:.2f} C".format(SENSOR_LOCATION_NAME, cpu_temp))
    humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

    if METRIC_UNITS:
        print("{} Temperature {:.2f} C".format(SENSOR_LOCATION_NAME, temp_c))
    else:
        temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")

    print("{} Humidity {} %".format(SENSOR_LOCATION_NAME, humidity))

    # TODO: allow farenheit temp
    data_row = '{},{},{},{},{}\n'.format(SENSOR_LOCATION_NAME, sys_time,
                                         cpu_temp, humidity, temp_c)
    with open(CSV_FILE, 'a') as f:
        f.write(data_row)

    time.sleep(60.0 * MINUTES_BETWEEN_READS)
