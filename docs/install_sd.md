# Install the SD Card

1. [Download the prebuilt image here.](https://www.dittserver.de/download/piease)
2. [Install the official Raspberry Pi Imager](https://www.raspberrypi.com/software/), to write the Image on a SD Card (16GB)
3. Open the Application and choose OS, scroll down to "Use Custom" and open the latest PiEase .img

![logo](images/getting_started/choose_os.png ':size=450')

![logo](images/getting_started/custom.png ':size=450')

?> Choose the downloaded ```piease_{latest}.img``` file from PiEase and then your Storage Device

![logo](images/getting_started/choose_and_write.png ':size=450')

# Setup WIFI

!> After finishing the setup you need to create a "wpa_supplicant.conf" on the SD Card **if you want to connect your Raspberry Pi with WIFI**

Just create a file called "wpa_supplicant.conf" directly on the SD Card with following content:

```shell
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=DE
network={
   ssid="{YOUR SSID}"
   psk="{YOUR SSID PASSWORD}"
}
```

## 5. That`s it. Insert the SD Card in your Raspberry and start it.




