# import warnings too
import warnings

# ignore actual warnings / there is a problem with the GPiO Module. This will updatet in the future!
warnings.filterwarnings('ignore')

# import gpiozero
from gpiozero import LED
import time

# init Device (Relay or LED or other GPIO Device)
led = LED(17)

# switch it on
led.on()

# wait one second
time.sleep(1)

# switch it off
led.off()
