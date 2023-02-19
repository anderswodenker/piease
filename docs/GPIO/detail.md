# GPIO (on/off)

## Usage

### Main function

Just use the [gpiozero](https://gpiozero.readthedocs.io/en/stable/recipes.html) module. It is pre-installed on the Image.

```python
# Import GPIO library
from sensorlib.gpio import Device

# init your device with GPIO and Name
device = Device(21, "relay")

# switch your device on or off
device.off()

```

!> If you name your Device "relay", .on() will be GPIO.LOW and .off() is GPIO.HIGH
