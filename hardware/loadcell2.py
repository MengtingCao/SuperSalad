import RPi.GPIO as GPIO
from hx711 import HX711

EMULATE_HX711=False

GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=5, pd_sck_pin=6)
#hx.zero()

reading = hx.get_data_mean(readings=40)
ratio = reading / float(360)
#ratio = 184.7111111111111
hx.set_scale_ratio(ratio)
while True:
    weight = hx.get_weight_mean()
    print(weight)
    print("ratio" + str(ratio))
