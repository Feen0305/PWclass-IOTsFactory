import time
import network
import dht
import ssd1306
from machine import Pin, I2C
from umqtt.simple import MQTTClient


# Define MQTT credentials
SERVER = "mqtt3.thingspeak.com"
CLIENT_ID = "LBweFyIOJRQtMDUXJgMGGzM"
USER = "LBweFyIOJRQtMDUXJgMGGzM"
PASS = "6N/wvQHIM83GVBdz4huNSTMX"
CH_ID = "2778045"

# Define OLED display
i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    wlan.connect("Wokwi-GUEST", "")
    while not wlan.isconnected():
        pass
print("Connected to Wi-Fi. IP Address: ", wlan.ifconfig()[0])

# Set up MQTT connection
client = MQTTClient(CLIENT_ID, server=SERVER, user=USER, password=PASS, keepalive=30)
client.connect()
topic = "channels/" + CH_ID + "/publish"

# Set up DHT22 sensor and LED
sensor1 = dht.DHT22(Pin(12))
led = Pin(2, Pin.OUT)

while True:
    try:
        # Measure data
        led.value(0)  # Turn off the LED before measurement
        sensor1.measure()
        temperature = sensor1.temperature()
        humidity = sensor1.humidity()
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

        # Update OLED display
        display.fill(0)
        display.text(f"Temp: {temperature}°C", 0, 0, 1)
        display.text(f"Humidity: {humidity}%", 0, 10, 1)
        display.show()

        # Prepare payload and publish data to Thingspeak
        payload = "field1=" + str(temperature) + "&field2=" + str(humidity)
        client.publish(topic, payload)
        print("Published:", payload)

        # Visual feedback using LED
        led.value(1)
        time.sleep(15)
        led.value(0)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
