# Load Cell

## Wiring

?> GND to GND | VCC to 5V | DT to GPIO 5 | SCK to GPIO 6

![schema](raspberry_load_cell.png ':size=450')

## Usage

### CALIBRATE AND GET DATA

```python
# import the LOAD CELL Library
from sensorlib.scale import Scale

# init your load cell
load_cell = Scale()

# calibrate with some weights
load_cell.calibrate(1000) # weight in Gramm

# get data from the load cell
load_cell_data = load_cell.get_data()
```