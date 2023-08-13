
from ds18b20 import DS18B20
from relay import Device
import time
from config import LocalConfig
# Initialisierung der Klasse
conf = LocalConfig()
sensor = DS18B20()

# Relais zuordnung der GPIO Pins
relay01 = Device(6, "relay")
relay02 = Device(13, "relay")
relay03 = Device(19, "relay")
relay04 = Device(26, "relay")


while True:
    # Laden der Werte aus der conf.ini
    conf.get_config_data()
    xs_temp = float(conf.settings['xs_temp'])
    xs_hysterese = float(conf.settings['xs_hysterese'])

    sensor_links = sensor.tempC(0)
    print(f"Temp_links {sensor_links}")
    if sensor_links < xs_temp:
        relay01.on()
    elif sensor_links > xs_temp + xs_hysterese:
        relay01.off()


    sensor_rechts = sensor.tempC(1)
    print(f"Temp_rechts {sensor_rechts}")
    if sensor_rechts < xs_temp:
        relay02.on()
    elif sensor_rechts > xs_temp + xs_hysterese:
        relay02.off()

    time.sleep(0.5)

