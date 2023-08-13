from datetime import datetime
from relay import Device
import time
from sunservice import get_sunset, get_sunrise

# Relais zuordnung der GPIO Pins
warming_light = Device(19, "relay") #wärmelampen (halogen) Relais 3
main_light = Device(26, "relay") #hauptlicht (röhre) Relais 4


while True:
    now = datetime.now().strftime("%H:%M")
    light_on = get_sunrise(0)
    light_off = get_sunset(0)

    if now == light_on:
        warming_light.on()
        time.sleep(60 * 15)
        main_light.on()

    if now == light_off:
        warming_light.off()
        time.sleep(60 * 15)
        main_light.off()

    time.sleep(30)



























# Zunächst ist die Aktivierung des Device Tree Overlay für 1-wire notwendig.
# Dazu editiert man (per sudo nano oder einem anderen Editor Ihrer Wahl)
# die Datei /boot/config.txt und fügt folgende Zeile hinzu:
# dtoverlay=w1-gpio,gpiopin=4



