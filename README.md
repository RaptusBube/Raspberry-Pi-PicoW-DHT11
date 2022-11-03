# Raspberry-Pi-PicoW-DHT11
Create a SmartHome-enabled temperature and humidity sensor with an Raspberry Pi Pico W and a DHT11 in python.

## Summary

1. [Requirements](#requirements)
2. [Hardware](#hardware)
3. [Download](#installation)
4. [MicroPython](#micropython)
5. [Upload to Pico](#upload-to-pico-w)
6. [Reset](#reset)
7. [HomeAssist Integration](homeassist-integration)

# Requirements
To make this project you need a Raspberry Pi Pico W, a DHT 11 temperature, humidity sensor and 3 bumper cables and a micro usb cabel / power supply to run it later seperatly from your computer. The DHT11 sensors with a circuit board are ideal, as the correct series resistors are already soldered onto them and do not have to be retrofitted. The following instructions refer to this type. In this tutorial, Thonny is used on Windows. Anyone is free to use another IDE and/or operating system. However, the functions shown in this tutorial may look slightly different and cannot be adopted one-to-one. In this case, it is best to look for solutions for your own IDE or use the software used in this tutorial.  

# Hardware

The DHT11 is connected to the Pico W with 3 cables. It needs 3.3V, GND and a GPIO pin once each. I would recommend pins 38, 36 and 34, as these are relatively close together and can therefore be connected in a space-saving way. **So we connect pin 38 on the pico to GND on the DHT11, pin 36 to VCC and pin 34 to DATA.** If you want to use a different pin, you are welcome to do so, but note that in the ```web-socket.py``` the pin of the DHT11 sensor must then be changed from 28 to the new pin. Note, however, that the programme does not indicate the number of the connection on the Pico W, but the number of the GP pin. (e.g. Pin 34 on the Pico W is GP Pin 28)

![image](https://user-images.githubusercontent.com/74785642/199821986-7d626d02-4a28-4926-be3b-98c163ac6d9a.png)

Now that you've wired them all up and soldered the bumper cables to the Pico W, it's time to power it up. The easiest way to do this is to connect the Pico W directly to your computer via micro USB. If your DHT11 has a status LED, it should now light up, in my case it was red. Now we have prepared the Pico W for everything and can continue with the installation of the software.

# Installation

Download the latest relase of my code [here](https://github.com/RaptusBube/Raspberry-Pi-PicoW-DHT11/releases/tag/v1.0.0) and unzip it to a new folder. Open the wifi.py file and change ```ssid```and ```password``` with your WIFI login data. 

# MicroPython

When you buy a new Pico, no firmware is installed on it yet. This must be installed first. Since our script is written in Python, we need the MicroPython firmware for the Raspberry Pi Pico W, which we can get [here](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2). While the Pico W has just been connected to the computer, it should have recognised it as a new drive. To do this, simply open the Explorer and navigate to the Pico W. There should already be two files in this directory, but they are negligible. To continue, we copy the MicroPython software we just downloaded into this directory. The Pico W should now automatically recognise the firmware and disconnect its own drive. If the Pico W is no longer visible in the Explorer, we can now proceed to the next step.   

# Upload to Pico W

To upload the code to your Raspberry Pi Pico W you will need an IDE like [Thonny](https://thonny.org). First, start Thonny and navigate with the mouse to the bottom right corner where the current interpreter (mostly Python 3.x.x) should be. Simply click on it and select MicroPython (Raspberry Pi Pico) from the list. If the file view is not yet open, this must first be opened. To do this, simply select the View tab at the top and click on Files. Two windows should now open, one with your own files on the computer and the other an empty window with the title Rapsberry Pi Pico. In the upper file window we now navigate to the folder where we just copied the downloaded source code. Now we right-click on each file except main.py and select ```Upload to /```. These files should now appear in the lower window which was just empty. Before we have everything ready, we briefly check that everything is working. To do this, we double-click on m.py to open it. With the green start button in the upper left corner (or F5) we start this script. If everything is configured correctly, you can expect the following console output: 
```
loading tempWebServer
starting WIFI CON
waiting for connection...
connected
ip = xxx.xxx.xxx.xxx
listening on ('0.0.0.0', 80)
```
If the WiFi connection is poor, it may take a little longer to establish a connection. However, if no connection can be established, the Pico will restart itself. Then simply select it again at the bottom right and run ```m.py``` again and, if necessary, select a different wifi or check the login data. To finally check the functionality, simply enter the IP address just output into the browser and the ```humidity:temperature``` should be displayed. If this is also successful, we can now prepare the Pico W for permanent use. To do this, we stop the Pico by selecting Stop (or CTRL + F2) at the top left. Now we copy the main.py with a right click on it and then ```Upload it to /``` on the Pico W. Then we can disconnect the micro USB cable from the Pico W. To start the Pico W now, simply connect it to power via micro USB and the programme will start by itself. 

**DEBUG:** While the Pico W is booting, the built-in LED of the Pico W will blink twice. After that the Pico W tries to connect to the WIFI. During this process, it glances once during each attempted connection. If the connection is established, the LED will light up permanently. If no WIFI connection can be established, the LED flashes 5 times and faster before the Pico W restarts and tries to establish a connection again. The red LED of the DHT11 should light up permanently.

# Reset

If, contrary to expectations, the software hangs or the password for the WiFi has changed, there is only one way to reset the Pico W and that is to detonate a nuke in the true sense of the word. First, the Pico W must be connected to the computer. However, while plugging in the USB cable, the BOOTSelect button on the Pico W must be pressed. The Pico W should now show up as a drive again. To reset the Pico W now, we need to unzip and then copy [this](https://github.com/RaptusBube/Raspberry-Pi-PicoW-DHT11/files/9933195/PicoW_Nuke.zip) firmware to the folder of the Pico W. The Pico W should now disconnect by itself and reconnect after a short time. After that, the Pico W should be treated as an unused Pico W and can be put on again according to the instructions.

# HomeAssist Integration

Now we can look at the temperature and humidity via a browser at any time, but this is not really smart yet. To make the Pico W sensor really smart, there is also its own integration in HomeAssist. Since this is a separate script, there is no ready-made integration for it in HomeAssist yet, yet integration is very easy. However, as an add-on we only need the HA Addon Studio Code Server (https://github.com/hassio-addons/addon-vscode). After installing this addon, open the custom user interface. In the left bar the Explorer should be selected and a list of files should appear. The relevant file for us is the configuration.yaml. Just open it and add the following part (it is a rest API configuration):  
```
rest:
  - resource: http://xxx.xxx.xxx.xxx/
    scan_interval: 10
    sensor:
      - name: NAMEOFYOUTTEMPSENSOR
        value_template: "{{ value.split(':')[1] }}"
        unit_of_measurement: "°C"
      - name: NAMEOFYOURHUMISENSOR
        value_template: "{{ value.split(':')[0] }}"
        unit_of_measurement: "%"
```
If more than one Pico W is to be used, multiple resources can simply be added. The variable scan_interval is used to specify the scan interval in seconds, which can be changed as desired. HomeAssist does not recognize these sensors directly, but they must be added individually to a dashboard. To do this, simply go to the settings on dashboards, click on add dashboard. After creating then click on this dashboard and click in the upper right corner on the three dots and select configure user interface. After that add a new map, select the tab by entity and search for the names you just assigned. If the names you just assigned do not show up, there is either an error with the REST API configuration (Then most of the time there is an error with the component in the home-assistant.log directly under the configuration.yaml file) or Studio Code Server has not passed them through yet. If this is the case, in most cases it helps to simply restart HomeAssist. After that the assigned names should swap in the entities list. 
