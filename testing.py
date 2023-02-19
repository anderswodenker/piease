# import the AHT20 Library
from sensorlib.aht20 import AHT20

# init your sensor
my_sensor = AHT20()

# get data from sensor
sensor_data = my_sensor.get_data()  # example:  {'temp':20, 'hum': 40}

print(sensor_data)
