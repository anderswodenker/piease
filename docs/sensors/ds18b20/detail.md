# DS18B20 (Temperature Sensor)

## Schema

![schema](schema_ds18b20.png ':size=450')

## Wiring

?> GND to GND | VDD to 3V | Data to GPIO 4

![schema](raspberry_ds18b20.png ':size=450')

!> It is possible to wire more than one Sensor. Just wire in a row! 🙂 

## Usage

### READ TEMPERATURE

```python
# import the DS18B20 Library
from sensorlib.ds18b20 import DS18B20

# init your sensor
my_sensors = DS18B20()

# get data from sensor with tempC
temperature = my_sensors.tempC(0) # 0 is the first Sensor. If you have more than one, just change the number (0, 1, 2, 3 ...)
```

### COUNT DEVICES

```python
# import the DS18B20 Library
from sensorlib.ds18b20 import DS18B20

# init your sensor
my_sensors = DS18B20()

# get number of devices
device_counts = my_sensors.device_count()
```

!> If you want to change the pin, use the following commands... 

```shell
    sudo dtoverlay w1-gpio gpiopin=4 pullup=0  # header pin 7
    sudo dtoverlay w1-gpio gpiopin=17 pullup=0 # header pin 11
    sudo dtoverlay w1-gpio gpiopin=27 pullup=0 # header pin 13
```

Thanks to [pinout.xyz](https://pinout.xyz/pinout/1_wire#)