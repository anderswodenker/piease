# RGB LED (Single one)

## Wiring

![schema](raspberry_rgb.png ':size=450')

## Usage

### Main function

```python
# import the RGB Library
from sensorlib.rgb import RGB

# init your LED
led = RGB()

# switch red on / off
led.red()
led.off()

# switch green on / off
led.green()
led.off()

# switch blue on / off
led.blue()
led.off()

# blink
led.blink("red", 3, 1) # color, times, seconds between

```

!> Feel free to optimize the library