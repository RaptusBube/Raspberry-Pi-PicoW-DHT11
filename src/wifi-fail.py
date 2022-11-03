from machine import Pin
import time
led = machine.Pin("LED", machine.Pin.OUT)
led.off()
time.sleep(20)
exec(open("wifi.py").read())