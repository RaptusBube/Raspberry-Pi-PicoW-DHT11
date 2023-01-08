import network
import time
import time
import machine
print("starting WIFI CON")
led = machine.Pin("LED", machine.Pin.OUT)
led.off()
ssid = 'YOURWFISSID'
password = 'YOURWIFIPASSWORD'

wlan = network.WLAN(network.STA_IF)
wlan.active(False)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
  led.on()
  if wlan.status() < 0 or wlan.status() >= 3:
    break
  max_wait -= 1
  print('waiting for connection...')
  time.sleep(1)
  led.off();
  time.sleep(1)

if wlan.status() != 3:
  print('network connection failed')
  exec(open("error.py").read())
else:
  led.on()
  print('connected')
  status = wlan.ifconfig()
  print( 'ip = ' + status[0] )
  exec(open("web-socket.py").read())

