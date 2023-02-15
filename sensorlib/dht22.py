import adafruit_dht
from helper.log_helper import ErrorHandler
import board
import time


class DHT22:
    def __init__(self):
        self.data = {}
        self.sensor = adafruit_dht.DHT22(board.D3)

    def get_data(self):
        attempts = 0
        while attempts <= 3:
            try:
                self.data = {"temp": float(self.sensor.temperature), "hum": float(self.sensor.humidity)}
                if self.data:
                    return self.data
                else:
                    attempts = attempts + 1
            except RuntimeError as error:
                print(error.args[0])
                attempts = attempts + 1
                time.sleep(2.0)
                continue

            except Exception as e:
                print(e)
                self.sensor.exit()
                return False
