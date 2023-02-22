import os
from fileinput import input

os.system("sudo chown root:$USER /dev/gpiomem")
os.system("sudo chmod g+rw /dev/gpiomem")

import RPi.GPIO as GPIO
import time
import signal
import sys

# Configuration
DEFAULT_PIN = 18  # BCM pin used to drive PWM fan
WAIT_TIME = 1  # [s] Time to wait between each refresh
PWM_FREQ = 25  # [kHz] 25kHz for Noctua PWM control

# Configurable temperature and fan speed
freq = 0
try:
    # Setup GPIO pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DEFAULT_PIN, GPIO.OUT, initial=GPIO.LOW)
    fan = GPIO.PWM(DEFAULT_PIN, PWM_FREQ)
    fan.start(int(freq))

except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()  # resets all GPIO ports used by this function
    exit()

