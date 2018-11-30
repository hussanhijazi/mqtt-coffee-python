import paho.mqtt.client as mqtt
from variables import *

def on_message(client, userdata, message):
    print("Python: ", message.topic, " - ", str(message.payload.decode("utf-8")))
    actual_state = str(message.payload.decode("utf-8"))
    client.unsubscribe(coffee_topic)
    send_state = ""
    if(actual_state == "off"): 
        send_state = "on"
    else:
        send_state = "off"
    client.publish(coffee_topic, send_state, 0, True)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(coffee_topic)

def on_publish(client, userdata, mid):
    client.disconnect()

def mqtt_client_connect():
    print("connected to: ", broker_url)
    client.connect(broker_url)
    client.loop_forever()
    
client = mqtt.Client("client_name")
client.on_connect = on_connect
client.on_message = on_message 
client.on_publish = on_publish 

mqtt_client_connect()
