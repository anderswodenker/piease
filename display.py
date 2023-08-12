import sys
import os
from sensorlib.scale import Scale

scale = Scale()
counter = 0
picdir = '/home/pi/piease/pic/'

import logging
import epd2in9_V2
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in9 V2 Demo")
    epd = epd2in9_V2.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    font24 = ImageFont.truetype('Roboto-Regular.ttf', 24)
    font18 = ImageFont.truetype('Roboto-Regular.ttf', 18)

    # partial update
    logging.info("5.show time")
    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)
    epd.display_Base(epd.getbuffer(time_image))
    num = 0

    while True:
        scale_data = scale.get_data()
        time_draw.rectangle((10, 10, 120, 50), fill=255)
        time_draw.text((10, 10), str(scale_data), font=font24, fill=0)
        newimage = time_image.crop([10, 10, 120, 50])
        time_image.paste(newimage, (10, 10))
        epd.display_Partial(epd.getbuffer(time_image))

        num = num + 1
        if (num == 10):
            break

    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)

    logging.info("Goto Sleep...")
    epd.sleep()

except Exception as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in9_V2.epdconfig.module_exit()
    exit()
