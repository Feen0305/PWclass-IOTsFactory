import time
from machine import Pin

sw1 = Pin(12, Pin.IN)
count = 0

while(1):
  val = sw1.value()
  if(val == 0):
    count+= 1
    print(count)
  time.sleep(0.2)