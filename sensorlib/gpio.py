"""
based on https://pypi.org/project/RPi.GPIO/
edited to make it a little easier to use the DHT22 Sensor
written by anderswodenker
"""
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Device:
    def __init__(self, pin, device_type):
        """
        :param pin: int (GPIO)
        :param device_type: string (Name of the device)
        """
        self.pin = pin
        self.type = device_type

    def on(self):
        """
        set the GPIO PIN to HIGH or LOW
        """
        GPIO.setup(self.pin, GPIO.OUT)
        if self.type == "relay":
            GPIO.output(self.pin, GPIO.LOW)
        else:
            GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        """
        set the GPIO PIN to HIGH or LOW
        """
        GPIO.setup(self.pin, GPIO.OUT)
        if self.type == "relay":
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            GPIO.output(self.pin, GPIO.LOW)
