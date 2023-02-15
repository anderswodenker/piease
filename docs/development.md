# Quick Start Guide

!> Find your Raspberry Pi IP Adresse first. It depends on your Network and Router configurations. I work here with ```192.168.0.13``` as an Example. There are many Guides to find the Adresse out there.

1. Use or Install a Coding IDE like [Visual Studio Code](https://code.visualstudio.com/), or [PyCharm](https://www.jetbrains.com/de-de/pycharm/)
2. Connect your IDE with the RaspberrPi. **PiEase ist found on ```/home/pi/piease/```**
3. [Clone]() the PiEase Framework

?> **You don`t need to install a virtual environment. Develop on your Desktop and compile on your Raspberry Pi. Just upload your files in the PiEase Project. PyCharm and VisualStudio Code has an automatic Upload function**

4. Browse to your RaspberrPi IP Adresse ```http://192.168.0.13```
5. You can see a pre installed WebApp with some Examples.

### It is easy to customize the web app! Or Install an own app.


#### Here are some examples how easy...


```python
# READ TEMPERATUR FROM a DS18B20 Sensor

from sensorlib.ds18b20 import DS18B20

my_sensor = DS18B20()  # init your DS18B20 Sensor

# print the sensors value in Celsius
print(my_sensor.tempC(0))  # 0 is for the first Sensor
```

```python
# TURN A RELAY ON AND OFF

from sensorlib.gpio import Device
import time

# init your new Device with a GPIO Pin and Name
my_device = Device(18, 'relay')  

# switch device on
my_device.on()

# wait 5 Seconds
time.sleep(5)

# switch device off
my_device.off()
```


# Yes, it is that easy!