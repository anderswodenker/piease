import os
import time
import matplotlib.pyplot as plt
from configuration.local_config import LocalConfig
from sensorlib.scale import Scale


def main():
    config = LocalConfig()
    scale = Scale()
    config.get_config_data()

    if not config.scale["calibrated"]:
        setup_scale(scale)
        calibrate_scale(scale)

    read_data = input("Do you want to read the Scale data? (y/n): ").lower()

    if read_data == "y":
        display_scale_data(scale)


def setup_scale(scale):
    input("Please remove all items from the Scale and press Enter...")
    print("Setting up the Scale...")
    scale.setup()
    print("Done!\n")


def calibrate_scale(scale):
    calibrate_weight = int(input("Enter the calibration weight (in grams), put it on the Scale, and press Enter: "))
    print("Calibrating Scale...")
    scale.calibrate(calibrate_weight)
    print("Done!\n")


def display_scale_data(scale):
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots()
    scale_data = []

    try:
        while True:
            data = scale.get_data()
            print(f"{data}g")
            scale_data.append(data)

            ax.clear()
            ax.plot(scale_data)
            ax.set_title("Scale Data")
            ax.set_xlabel("Time")
            ax.set_ylabel("Weight (g)")

            plt.pause(1.5)  # Pause for a short period to allow the plot to update
    except Exception as e:
        print(e)
        plt.ioff()  # Disable interactive mode


if __name__ == "__main__":
    main()
