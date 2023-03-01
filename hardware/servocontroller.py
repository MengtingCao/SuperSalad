# TODO: work on Raspberry Pi environment setup

from adafruit_pca9685 import PCA9685 # pip3 install adafruit-circuitpython-pca9685

from time import sleep
from board import SCL, SDA
import busio

from adafruit_motor import servo

NUM_SERVOS = 10


class ServoController:
    def __init__(self):
        self._i2c_bus = busio.I2C(SCL, SDA)
        self._pca = PCA9685(i2c_bus, address=0x40)
        self._pca.frequency = 50
    
        self._servos = []
        for i in range(NUM_SERVOS):
            self._servos.append(servo.ContinousServo(self._pca.channels[i]))

    # for FT90 servos, only need to worry about -1.0, 0, 1.0 speeds. Also, we should only have to deal with either -1.0 or 1.0, depending on how the servos are mounted
    def setServoThrottle(self, servoIndex: int, throttle: float):
        assert(servoIndex >= 0 and servoIndex < NUM_SERVOS)
        assert(throttle >= -1.0 and throttle <= 1.0)

        self._servos[i].throttle = throttle
    
def main():
    # just some test code
    # start and stop each servo for 1 second
    servoController = ServoController()
    for i in range(NUM_SERVOS):
        servoController.setServoThrottle(i, 1.0)
        sleep(1.0)
        servoController.setServoThrottle(i, 0.0)
        sleep(1.0)

if __name__ == '__main__':
    main()