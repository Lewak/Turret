
from laser import Laser
from gimbal import Gimbal
from motion_sensor import MotionSensor
from gpio_interface import GpioInterface
from audio_interface import AudioInterface


class Peripherals:

    motion_sensor = None
    laser = None
    gimbal = None
    audio = None

    @staticmethod
    def initialise():
        GpioInterface.initialise()
        Peripherals.motion_sensor = MotionSensor(14)
        Peripherals.laser = Laser(4)
        Peripherals.gimbal = Gimbal(3, 2)
        Peripherals.audio = AudioInterface()
        Peripherals.laser.turnOff()

    @staticmethod
    def destroy():
        GpioInterface.destroy()
        Peripherals.laser.turnOff()
        Peripherals.gimbal.destroy()

