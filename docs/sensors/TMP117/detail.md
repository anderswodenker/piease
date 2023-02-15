# TMP117 (High Precision Temperature)

## Wiring

?> GND to GND | VDD to 3V | SCL to GPIO 4 | SCL to GPIO 2

![schema](raspberry_tmp117.png ':size=450')

!> Look at [Adafruit](https://learn.adafruit.com/adafruit-tmp117-high-accuracy-i2c-temperature-monitor/overview) for further information

## Usage

### READ TEMPERATURE AND HUMIDITY

```python
# import the TMP117 Library
from sensorlib.tmp117 import TMP117

# init your sensor
my_sensor = TMP117()

# get data from sensor 
sensor_data = my_sensor.get_data() # example:  {'temp':20}
```