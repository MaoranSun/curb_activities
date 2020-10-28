import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.publish("RATP", json.dumps('{message: "Hello from python!"}'))
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

#client.loop_forever()

count = 0
while count < 10:
    count += 1
    client.publish("RATP", count)