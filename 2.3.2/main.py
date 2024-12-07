import time
import dht
from machine import Pin

# define sensor pin at D12
Sensor1 = dht.DHT22(Pin(12))

led= Pin(2, Pin.OUT)

while(1):
    # measure
    led.value(1)
    Sensor1.measure()
    temperature = Sensor1.temperature()
    humidity = Sensor1.humidity()
    led.value(0)

    # print data
    print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

    # delay a while
    time.sleep(1)
