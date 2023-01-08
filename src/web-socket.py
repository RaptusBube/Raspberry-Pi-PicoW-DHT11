import socket
from machine import Pin, I2C
from dht import DHT11, InvalidChecksum
html = """%s"""
try:
    dht11_sensor = DHT11(Pin(28, Pin.IN, Pin.PULL_UP)) #Change to your Pin if necessary 
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('listening on', addr)
    lasthumi = dht11_sensor.humidity
    lasttemp = dht11_sensor.temperature
    while True:
      try:
          cl, addr = s.accept()
          try:
              temp = dht11_sensor.temperature
              humi = dht11_sensor.humidity
              lasttemp = temp
              lasthumi = humi
          except Exception as EX:
              humi = lasthumi
              temp = lasttemp
          request = cl.recv(1024)
          request = str(request)
          cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n')
          cl.send(html % str(humi)+":"+str(temp))
          cl.close()
      except OSError as e:
        cl.close()
        print(e)
        print('connection closed')

except Exception as e:
    print(e)
    exec(open("error.py").read())
