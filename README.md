# SuperSalad
Public facing gui interface git repo for Super Salad group Customizable Food Dispenser


## Hardware Prerequisites

1. Install Circuit Python

```
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```

2. Install PCA9685 (Servo Driver Board)

```
pip3 install adafruit-circuitpython-pca9685
```

3. Install HX711 (Weight Sensor)

```
pip3 install 'git+https://github.com/gandalf15/HX711.git#egg=HX711&subdirectory=HX711_Python3'
```