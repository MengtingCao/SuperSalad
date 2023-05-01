import RPi.GPIO as GPIO
from hx711 import HX711 # pip3 install 'git+https://github.com/gandalf15/HX711.git#egg=HX711&subdirectory=HX711_Python3'

class WeightSensor:
    def __init__(self, dout_pin=5, pd_sck_pin=6, calibration_factor=1):
        GPIO.setmode(GPIO.BCM)
        print(calibration_factor)

        self._hx711 = HX711(
            dout_pin=dout_pin, 
            pd_sck_pin=pd_sck_pin,
            gain_channel_A=128,
            select_channel='A')

        # TODO: determine cal factor with a known weight
        self.calibration_factor = calibration_factor

        self._hx711.reset()
        err = self._hx711.zero() # zero the scale to account for weight of plate, etc.
        if err:
            raise ValueError('Unable to zero scale')

    def getRawMeasurement(self):
        value = self._hx711.get_raw_data_mean(readings=30)
        return value

    def getWeight(self):
        value = self._hx711.get_weight_mean(readings=30)
        return value

    def calibrate(self, knownWeight):
        data = self._hx711.get_data_mean(readings=30)
        self.calibration_factor = data / knownWeight
        self._hx711.set_scale_ratio(self.calibration_factor)
        print(self.calibration_factor)
        return self.calibration_factor


def ws_main():
    # just some test code
    weightSensor = WeightSensor(calibration_factor=1342.9942528735633)
    calWeight = float(input("Enter cal weight and add weight: "))
    res = weightSensor.calibrate(calWeight)
    print(res)
    input("remove weight")
    weightSensor._hx711.zero()
    while(True):
        print(weightSensor.getRawMeasurement(), weightSensor.getWeight())

    
if __name__ == '__main__':
    ws_main()