#!/bin/sh

cat /dev/ttyS1 | mosquitto_pub -t servoControl -l
