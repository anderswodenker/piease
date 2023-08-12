# import the LOAD CELL Library
from sensorlib.scale import Scale
import time

# init your load cell
load_cell = Scale()

# set up the load cell
#load_cell.setup()

#calibrate_with = input("Calibrate with: ")

#load_cell.calibrate(int(calibrate_with)) # weight in Gramm

# get data from the load cell
# load_cell_data = load_cell.get_data()
while True:
 load_cell_data = load_cell.get_data()
 print(load_cell_data)
 time.sleep(1)
