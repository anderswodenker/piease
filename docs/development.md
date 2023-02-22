# Quick Start Guide

!> Find your Raspberry Pi IP Adresse first. It depends on your Network and Router configurations. I work here with ```192.168.0.13``` as an Example. There are many Guides to find the Adresse out there.

1. [Clone](https://github.com/anderswodenker/piease) the PiEase Framework and open it with your favorite IDE like [Visual Studio Code](https://code.visualstudio.com/), or [PyCharm](https://www.jetbrains.com/de-de/pycharm/)
2. Connect to the Raspberry Pi over ssh
```shell
ssh pi@192.168.0.13
```

?> **The Password is "piease"**

- In PyCharm and VisualStudio Code it is possible to connect the Repo directly over SFTP with the Raspberry Pi. This is easier and a time safer!
- **If you need help or some pro tips, check out my [patreon](patreon.com/piease)**


!> **Activate the "home/pi/piease/venv" before testing your code.**

```shell
source venv/bin/activate
```
deactivate the Virtual Environment:

```shell
deactivate
```



### Try to build your owm App! See the docs and play with the testing.py and some sensors, to see how easy it is.

## WebApp

```
http://192.168.0.13 
```

This URL opens the preinstalled WebApp (This IP is an example). 

```shell
restart_flask
```

Restarts the Flask Server