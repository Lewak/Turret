import time
import atexit
from laser import Laser
from gimbal import Gimbal
from motion_sensor import MotionSensor
from random_path_generator import randomPathGenerator
from gpio_interface import GpioInterface
from audio_interface import AudioInterface
from audio_interface import SoundTypes
import os, sys

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
audio.playRandomEffect(SoundTypes.SEARCHING)
time.sleep(2)
audio.playRandomEffect(SoundTypes.TARGETLOST)
time.sleep(2)
audio.playRandomEffect(SoundTypes.SEARCHING)
time.sleep(2)
audio.playRandomEffect(SoundTypes.TARGETLOST)


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
        #gimbal.setPosition(90, 90)
        played2 = 0
        if played == 0:
            audio.playRandomEffect(SoundTypes.SEARCHING)
            played = 1

    else:
        laser.turnOff()
        played = 0
        if played2 == 0:
            audio.playRandomEffect(SoundTypes.TARGETLOST)
            played2 = 1

    # laser.turnOn()
    # time.sleep(1)
    # laser.turnOff()
    # gimbal.setPosition(90, 90)
    # time.sleep(1)
