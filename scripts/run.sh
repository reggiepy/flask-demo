#!/bin/bash

LOG_PATH=/var/log/virt_device
echo $LOG_PATH
mkdir $LOG_PATH -p

cd /opt/flask-demo/ && exec python -m flask-demo/run  > "$LOG_PATH/flask-demo.log" 2>&1 &
