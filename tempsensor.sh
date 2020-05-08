#!/usr/bin/env bash

echo "activating env"
source /home/pi/code/climate-sensor/venv/bin/activate
echo "running tempsensor.py"
python /home/pi/code/climate-sensor/tempsensor.py
