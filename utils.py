# Sample code from https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python
import random
import time
import Adafruit_DHT
from gpiozero import CPUTemperature


# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
# CONNECTION_STRING = ""

# # Define the JSON message to send to IoT Hub.
# MEASURE_TYPE = "Simulated"
# MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity},"measure_type": {measure_type}}'


def iothub_client_init(connection_string):
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(connection_string)
    return client


def prepare_iot_hub_message(format_string, message_data):
    return format_string.format(**message_data)


def iothub_client_send_telemetry(client, message):
    print("Sending message: {}".format(message))
    client.send_message(message)
    print("Message successfully sent")
    # TODO: Allow custom properties and configure in config
    # # Add a custom application property to the message.
    # # An IoT hub can filter on these properties without access to the message body.
    # if temperature > 30:
    #     message.custom_properties["temperatureAlert"] = "true"
    # else:
    #     message.custom_properties["temperatureAlert"] = "false"


def read_temp_sensor(sensor=Adafruit_DHT.DHT22, pin_number=4):
    humidity, temp_c = Adafruit_DHT.read_retry(sensor, pin_number)
    # TODO: add option to return farenheit
    return humidity, temp_c


def read_pi_core_temp():
    return CPUTemperature().temperature
