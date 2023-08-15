# import os
#
# os.system("sudo chown root:$USER /dev/gpiomem")
# os.system("sudo chmod g+rw /dev/gpiomem")
#
# import RPi.GPIO as GPIO
# import time
# import signal
# import sys
#
# # Configuration
# DEFAULT_PIN = 18  # BCM pin used to drive PWM fan
# WAIT_TIME = 1  # [s] Time to wait between each refresh
# PWM_FREQ = 3  # [kHz] 25kHz for Noctua PWM control
#
# # Configurable temperature and fan speed
#
# freq = 0
# try:
#     # Setup GPIO pin
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(DEFAULT_PIN, GPIO.OUT, initial=GPIO.LOW)
#     led = GPIO.PWM(DEFAULT_PIN, PWM_FREQ)
#     while True:
#         freq = input('freq: ')
#         led.start(int(freq))
#         time.sleep(5)
#
# except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
#     exit()
#     # GPIO.cleanup() # resets all GPIO ports used by this function

import time
import RPi.GPIO as GPIO
from config import LocalConfig

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
conf = LocalConfig()

p = GPIO.PWM(18, 1000)  # kHz
p.start(0)
try:
    while True:
        conf.get_config_data()
        ds_cycle = float(conf.settings['ds_cycle'])
        p.ChangeDutyCycle(ds_cycle)
        time.sleep(2)
except KeyboardInterrupt:
    pass
    p.stop()
    GPIO.cleanup()
