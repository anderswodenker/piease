# AHT20 (Temperature / Humidity Sensor)

## Wiring

?> GND to GND | VDD to 3V | SCL to GPIO 3 | SDA to GPIO 2

![schema](raspberry_aht20.png ':size=450')

!> Look at [Adafruit](https://learn.adafruit.com/adafruit-aht20/python-circuitpython) for further information

## Usage

### READ TEMPERATURE AND HUMIDITY

```python
# import the AHT20 Library
from sensorlib.aht20 import AHT20

# init your sensor
my_sensor = AHT20()

# get data from sensor 
sensor_data = my_sensor.get_data() # example:  {'temp':20, 'hum': 40}
```