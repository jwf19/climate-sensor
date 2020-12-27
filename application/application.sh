#!/usr/bin/env bash

echo "activating env"
source /home/pi/code/climate-sensor/env/bin/activate
echo "changing into directory"
cd /home/pi/code/climate-sensor/application
export FLASK_APP=application.py
echo "running application"
flask run -h 192.168.1.161
