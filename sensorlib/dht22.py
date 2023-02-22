"""
original source https://learn.adafruit.com/dht/dht-circuitpython-code
edited to make it a little easier to use the DHT22 Sensor
written by anderswodenker
"""
import adafruit_dht
import board


class DHT22:
    def __init__(self):
        self.data = {}
        # change the board GPIO here if necessary
        self.sensor = adafruit_dht.DHT22(board.D21, use_pulseio=False)

    def get_data(self):
        """
        returns the data from the sensor
        :return: dict (temperature and humidity)
        """
        try:
            data = {"temp": float(self.sensor.temperature), "hum": float(self.sensor.humidity)}
            self.sensor.exit()
            return data
        except Exception as e:
            print(e)
            return False
