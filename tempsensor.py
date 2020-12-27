import time
from datetime import datetime
import yaml
import utils


# ------- User Settings ---------
with open("./sensor_config.yaml", "r") as cfg:
    config = yaml.load(cfg, Loader=yaml.FullLoader)

SENSOR_LOCATION_NAME = config["SENSOR_LOCATION_NAME"]
MINUTES_BETWEEN_READS = config["MINUTES_BETWEEN_READS"]
CSV_FILE = "./sensor_readings.csv"
AZURE_CONN_STR = config["AZURE"]["IOT_CONN_STR"].replace(' ', '')  # TODO: config loader func
AZURE_MSG_TEXT = config["AZURE"]["MSG_TXT"]

# -------------------------------
# Connect to Azure
iot_client = utils.iothub_client_init(AZURE_CONN_STR)

# Log data until interrupted
while True:
    sys_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu_temp = utils.read_pi_core_temp()
#    print("\n{} System Time {}".format(SENSOR_LOCATION_NAME, sys_time))
#    print("{} CPU Temperature {:.2f} C".format(SENSOR_LOCATION_NAME, cpu_temp))

    humidity, temp_c = utils.read_temp_sensor()
#    print("{} Temperature {:.2f} C".format(SENSOR_LOCATION_NAME, temp_c))

#    print("{} Humidity {} %".format(SENSOR_LOCATION_NAME, humidity))

    # TODO: allow farenheit temp and configure in config
    # TODO: supersede separate csv logging and send all to Azure
    data_row = '{},{},{},{},{}\n'.format(SENSOR_LOCATION_NAME, sys_time,
                                         cpu_temp, humidity, temp_c)
    with open(CSV_FILE, 'a') as f:
        f.write(data_row)

    # Send to IoT hub in the cloud
    message_data = {
        'temperature': temp_c, 'humidity': humidity,
        'location': SENSOR_LOCATION_NAME, 'system_time': sys_time,
        'cpu_temperature': cpu_temp
    }
    iot_message = utils.prepare_iot_hub_message(AZURE_MSG_TEXT,
                                                message_data)
    utils.iothub_client_send_telemetry(iot_client, iot_message)

    time.sleep(60.0 * MINUTES_BETWEEN_READS)
