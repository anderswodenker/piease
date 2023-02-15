# GPIO (on/off)

## Usage

### Main function

```python
# import the GPIO Library
from sensorlib.gpio import Device

# init your Device with the GPIO Number and the Name
my_device = Device(18, "relay")

# switch device on
my_device.on()

# switch device off
my_device.off()
```

!> The Name of the Device makes a diffrence. If you name your Device "led", it will turn on and off the LED. (High and
Low on the Pin are switched)