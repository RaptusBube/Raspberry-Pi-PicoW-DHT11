import socket
from machine import Pin
from dht import DHT11
# Select the onboard LED
html = """%s"""
try:
    dht11_sensor = DHT11(Pin(28, Pin.IN, Pin.PULL_UP))
    #Open socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    # Listen for connections
    while True:
      try:
          cl, addr = s.accept()
          dht11_sensor.measure()
          temp = dht11_sensor.temperature()
          humi = dht11_sensor.humidity()
          request = cl.recv(1024)
          #print(request)
          request = str(request)

          cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n')
          cl.send(html % str(humi)+":"+str(temp))
          #send = "HEYYY: "+str(count)
          #cl.send(html % str(humi)+":"+str(temp))
          #cl.send(send)
          cl.close()

      except OSError as e:
        cl.close()
        print(e)
        print('connection closed')

except Exception as e:
    print(e)
    exec(open("error.py").read())
