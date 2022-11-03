from machine import Pin
import time
led = machine.Pin("LED", machine.Pin.OUT)
t = 0
while t < 5:
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
    t+=1
machine.reset();

