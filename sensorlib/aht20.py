"""
original source https://learn.adafruit.com/adafruit-aht20
edited to make it a little easier to use the AHT20 Sensor
written by anderswodenker
"""
import board
import adafruit_ahtx0


class AHT20:
    def __init__(self):
        try:
            self.sensor = adafruit_ahtx0.AHTx0(board.I2C())
        except Exception as e:
            print(e)

    def get_data(self):
        """
        returns the data from the sensor
        :return: dict (temperature and humidity)
        """
        try:
            temp = self.sensor.temperature
            hum = self.sensor.relative_humidity

            data = {"temp": round(float(temp), 2), "hum": round(float(hum), 2)}
            return data
        except Exception as e:
            print(e)
            return False
