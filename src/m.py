import time
import machine
print("loading...")
def startwifi():
    try:
        led = machine.Pin("LED", machine.Pin.OUT)
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
        exec(open("wifi.py").read())
    except Exception as e:
        print("Failed to load wifi\n", e)
        exec(open("error.py").read())
startwifi()


