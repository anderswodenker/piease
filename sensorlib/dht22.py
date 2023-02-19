import adafruit_dht
import board
import time


class DHT22:
    def __init__(self):
        self.data = {}
        self.sensor = adafruit_dht.DHT22(board.D21, use_pulseio=False)

    def get_data(self):
        try:
            data = {"temp": float(self.sensor.temperature), "hum": float(self.sensor.humidity)}
            self.sensor.exit()
            return data
        except:
            pass
