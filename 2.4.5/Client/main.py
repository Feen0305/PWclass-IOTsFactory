import time
import network
from umqtt.simple import MQTTClient


# Define MQTT credentials
SERVER = "mqtt3.thingspeak.com"
CLIENT_ID = "LBweFyIOJRQtMDUXJgMGGzM"
USER = "LBweFyIOJRQtMDUXJgMGGzM"
PASS = "6N/wvQHIM83GVBdz4huNSTMX"
CH_ID = "2778045"

topic = "channels/" + CH_ID + "/publish"

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    wlan.connect("Wokwi-GUEST", "")
    while not wlan.isconnected():
        pass
print("Connected to Wi-Fi. IP Address: ", wlan.ifconfig()[0])

# subscribe callback
def sub_cb(topic_t, msg):
    print(topic_t)
    print(msg)

    client.publish(topic, f"field1={msg}")

# Set up MQTT connection
client = MQTTClient(CLIENT_ID, server=SERVER, user=USER, password=PASS, keepalive=30)
client.set_callback(sub_cb)
client.connect()

# Subacribe to topic
client.subscribe('channels/' + CH_ID + '/subscribe/fields/field3')

while True:
    try:
        client.check_msg()

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
