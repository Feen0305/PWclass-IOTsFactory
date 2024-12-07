import time
from machine import Pin

p2 = Pin(2, Pin.OUT)

while True:
  p2.value(1)
  time.sleep(0.3)
  p2.value(0)
  time.sleep(0.3)