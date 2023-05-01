# TODO: work on Raspberry Pi environment setup

from adafruit_pca9685 import PCA9685 # pip3 install adafruit-circuitpython-pca9685

from time import sleep
from board import SCL, SDA
import busio

from adafruit_motor import servo

NUM_SERVOS = 10

class Servo(servo.ContinuousServo):

    @property
    def throttle(self) -> float:
        """How much power is being delivered to the motor. Values range from ``-1.0`` (full
        throttle reverse) to ``1.0`` (full throttle forwards.) ``0`` will stop the motor from
        spinning."""
        return self.fraction * 2 - 1

    @throttle.setter
    def throttle(self, value) -> None:
        # if value > 1.0 or value < -1.0:
        #     raise ValueError("Throttle must be between -1.0 and 1.0")
        # if value is None:
        #     raise ValueError("Continuous servos cannot spin freely")
        if value is None:
            self.fraction = None
        else:
            self.fraction = (value + 1) / 2
    
    


class ServoController:
    def __init__(self):
        self._i2c_bus = busio.I2C(SCL, SDA)
        self._pca = PCA9685(self._i2c_bus, address=0x40)
        self._pca.frequency = 50
    
        self._servos = []
        for i in range(NUM_SERVOS):
            self._servos.append(Servo(self._pca.channels[i]))

    # for FT90 servos, only need to worry about -1.0, 0, 1.0 speeds. Also, we should only have to deal with either -1.0 or 1.0, depending on how the servos are mounted
    def setServoThrottle(self, servoIndex: int, throttle):
        # assert(servoIndex >= 0 and servoIndex < NUM_SERVOS)
        # assert(throttle >= -1.0 and throttle <= 1.0)

        self._servos[servoIndex].throttle = throttle
    
def sc_main():
    # just some test code
    # start and stop each servo for 1 second
    servoController = ServoController()
    while True:
        for i in range(1):
            servoController.setServoThrottle(i, 1.0)
            sleep(1/16)
            servoController.setServoThrottle(i, 0)
            sleep(0.5)

if __name__ == '__main__':
    sc_main()