import time
from machine import Pin, ADC

knob = ADC(34)

while(1):
  val = knob.read()
  print(val)
  time.sleep(0.1)