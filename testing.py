# Test a DHT22
from sensorlib.dht22 import DHT22

my_dht22 = DHT22()

print('Testing my DHT22')

data = my_dht22.get_data()

print(f"Temperature is:  {data['temp']}")
print(f"The Humidity is: {data['hum']}")

print("It work`s!")