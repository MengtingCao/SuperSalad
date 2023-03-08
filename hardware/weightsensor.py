import RPi.GPIO as GPIO
from hx711 import HX711 # pip3 install 'git+https://github.com/gandalf15/HX711.git#egg=HX711&subdirectory=HX711_Python3'

class WeightSensor:
    def __init__(self, dout_pin=5, pd_sck_pin=6):
        GPIO.setmode(GPIO.BCM)

        self._hx711 = HX711(
            dout_pin=dout_pin, 
            pd_sck_pin=pd_sck_pin,
            gain_channel_A=128,
            select_channel='A')

        # TODO: determine cal factor with a known weight
        self.calibration_factor = 1 

        self._hx711.reset()
        err = self._hx711.zero() # zero the scale to account for weight of plate, etc.
        if err:
            raise ValueError('Unable to zero scale')

    def getRawMeasurement(self):
        value = self._hx711.get_raw_data_mean(readings=30)
        if value:
            return value
        else:
            raise ValueError('Unable to read raw data')

    def getWeight(self):
        value = self._hx711.get_weight_mean(readings=30)
        if value:
            return value
        else:
            raise ValueError('Unable to read weight')

    def calibrate(self, knownWeight):
        data = self.getRawMeasurement()
        self.calibration_factor = data / knownWeight
        self._hx711.set_scale_ratio(self.calibration_factor)


def ws_main():
    # just some test code
    weightSensor = WeightSensor()
    while(True):
        print(weightSensor.getRawMeasurement())

    
if __name__ == '__main__':
    ws_main()