import time
import atexit
from laser import Laser
from gimbal import Gimbal
from motion_sensor import MotionSensor
from random_path_generator import randomPathGenerator
from gpio_interface import GpioInterface
from audio_interface import AudioInterface
from audio_interface import SfxTypes
import os

GpioInterface.initialise()
motion_sensor = MotionSensor(14)
laser = Laser(4)
gimbal = Gimbal(3, 2)
generator = randomPathGenerator(0.0001, 90, 90)
laser.turnOn()
os.chdir('audio')
print(os.getcwd())
print("test")
print("Initialisation complete")
audio = AudioInterface()
played = 0
played2 = 0


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
        played2 = 0
        if played == 0:
            audio.playRandomEffect(SfxTypes.SEARCHING)
            played = 1

    else:
        laser.turnOff()
        played = 0
        if played2 == 0:
            audio.playRandomEffect(SfxTypes.TARGETLOST)
            played2 = 1