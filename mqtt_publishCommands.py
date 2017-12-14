import os, sys, getopt
import paho.mqtt.client as mqtt
from motors import Servo

# Main program to obtain the servo angle and publish to MQTT
def __main__():
        #Setup MQTT and Instantiate the Servo Motor
        mqttc = mqtt.Client()
        servoMotor = Servo(0, 500, 2500)
        ## Define the MQTT Callbacks
        # The callback for when the client receives a response from the Server
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+str(rc))
            mqttc.subscribe("servoControl")

        # Subscribe to the MQTT Topic
        def on_subscribe(client, userdata, mid, granted_qos):
            print("Subscribed: " + str(mid) + " " + str(granted_qos))

        # The callback when a publish message is received from the Server
        def on_message(client, userdata, msg):
            if msg.payload:
                print(msg.topic + ":: payload is " + str(msg.payload))
                servoMotor.setAngle(int(msg.payload))
                
        # The callback to disconnect and update the user
        def on_disconnect(client, userdata, rc):
            print("Disconnect From Server")

        #Assign the callbacks
        mqttc.on_message = on_message
        mqttc.on_connect = on_connect
        mqttc.on_subscribe = on_subscribe
        mqttc.on_disconnect = on_disconnect
        #Connects directly to the Omega
        mqttc.connect('127.0.0.1')
        # Continue the network infinite loop
        mqttc.loop_forever()

if __name__ == '__main__':
    __main__()
