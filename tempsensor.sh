#!/usr/bin/env bash

echo "activating env"
source /home/pi/code/climate-sensor/env/bin/activate
echo "changing into directory"
cd /home/pi/code/climate-sensor/
echo "running tempsensor.py"
python /home/pi/code/climate-sensor/tempsensor.py
