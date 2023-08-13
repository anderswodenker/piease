from ds18b20 import DS18B20
from relay import Device
import time
from config import LocalConfig

# Initialisierung der Klasse
conf = LocalConfig()
sensor = DS18B20()

# Relais zuordnung der GPIO Pins
relay01 = Device(6, "relay")  # heizmatte links
relay02 = Device(13, "relay")  # heizmatte rechts

while True:
    # Laden der Werte aus der conf.ini
    conf.get_config_data()
    xs_temp = float(conf.settings['xs_temp'])
    xs_hysterese = float(conf.settings['xs_hysterese'])

    sensor_links = sensor.tempC(0)
    if sensor_links < xs_temp:
        relay01.on()
    elif sensor_links > xs_temp + xs_hysterese:
        relay01.off()

    sensor_rechts = sensor.tempC(1)
    if sensor_rechts < xs_temp:
        relay02.on()
    elif sensor_rechts > xs_temp + xs_hysterese:
        relay02.off()

    time.sleep(30)

# Zunächst ist die Aktivierung des Device Tree Overlay für 1-wire notwendig.
# Dazu editiert man (per sudo nano oder einem anderen Editor Ihrer Wahl)
# die Datei /boot/config.txt und fügt folgende Zeile hinzu:
# dtoverlay=w1-gpio,gpiopin=4
