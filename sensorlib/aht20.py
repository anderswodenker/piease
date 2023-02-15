import board
import adafruit_ahtx0


class AHT20:
    def __init__(self):
        try:
            self.sensor = adafruit_ahtx0.AHTx0(board.I2C())
        except Exception as e:
            print("no AHT20!!!")
            print(e)

    def get_data(self):
        try:
            temp = self.sensor.temperature
            hum = self.sensor.relative_humidity

            data = {"temp": round(float(temp), 2), "hum": round(float(hum), 2)}
            return data
        except Exception as e:
            print(e)
            return False
