#!/bin/sh

cat /dev/ttyS1 | mosquitto_pub -t servoControl -l &
python /root/mqtt_servo_controller/mqtt_get_angle_publish.py
