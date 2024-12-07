import time
import dht
import ssd1306
from machine import Pin, I2C

# define sensor pin at D12
Sensor1 = dht.DHT22(Pin(12))

#define OLED
i2c = I2C(scl = Pin(4), sda = Pin(5), freq = 100000)
display = ssd1306.SSD1306_I2C(128,64, i2c)

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

    # Oled
    display.fill(0)
    display.text(f"Temp: {temperature}degC", 0, 0, 1)
    display.text(f"Humidity: {humidity}%", 0, 10, 1)
    display.show()

    # delay a while
    time.sleep(1)
