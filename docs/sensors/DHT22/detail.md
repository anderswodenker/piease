# DHT22 (Temperature and Humidity Sensor)

## Wiring

?> GND to GND | VDD to 3V | DATA to GPIO 2

![schema](raspberry_dht22.png ':size=450')

!> You can change the Data Pin if you want. Just change the Pinout in the dht22 Library as well. Default Pin ist GPIO 2 (Pin 3)

## Usage

### READ TEMPERATURE AND HUMIDITY

```python
# import the DS18B20 Library
from sensorlib.dht22 import DHT22

# init your sensor
my_sensor = DHT22()

# get data from sensor 
sensor_data = my_sensor.get_data() # example:  {'temp': 20, 'hum': 40}
```