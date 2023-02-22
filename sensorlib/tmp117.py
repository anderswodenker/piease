"""
original source https://learn.adafruit.com/adafruit-tmp117-high-accuracy-i2c-temperature-monitor
edited to make it a little easier to use the TMP117 Sensor
written by anderswodenker
"""
import board
import adafruit_tmp117


class TMP117:
    def __init__(self):
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.tmp117 = adafruit_tmp117.TMP117(i2c)

    def get_data(self):
        """
        returns the data from the sensor
        :return: dict (temperature and humidity)
        """
        try:
            return {'temp': round(float(self.tmp117.temperature), 2)}
        except Exception as e:
            print(e)
            return False
