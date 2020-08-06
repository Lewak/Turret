import time
import atexit
from laser import Laser
from gimbal import Gimbal
from motion_sensor import MotionSensor
from random_path_generator import randomPathGenerator
from gpio_interface import GpioInterface

GpioInterface.initialise()
motion_sensor = MotionSensor(14)
laser = Laser(4)
gimbal = Gimbal(3, 2)
generator = randomPathGenerator(0.0001, 90, 90)
laser.turnOn()
print("Initialisation completed")


def shutdownSystem() -> None:
    laser.turnOff()
    gimbal.destroy()
    GpioInterface.destroy()
    print("Shutdown complete")


atexit.register(shutdownSystem)

while True:
    if motion_sensor.isMotionDetected():
        laser.turnOn()
        tupla = next(generator)
        time.sleep(1/30)
        gimbal.setPosition(tupla[0], tupla[1])
    else:
        laser.turnOff()

    # laser.turnOn()
    # time.sleep(1)
    # laser.turnOff()
    # gimbal.setPosition(90, 90)
    # time.sleep(1)
