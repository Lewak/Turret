from laser import Laser
from gimbal import Gimbal
from motion_sensor import MotionSensor
from gpio_interface import GpioInterface
from audio_interface import AudioInterface
from button import Button


class Peripherals:
    motion_sensor: MotionSensor = None
    laser: Laser = None
    gimbal: Gimbal = None
    audio: AudioInterface = None
    button: Button = None

    @staticmethod
    def initialise():
        GpioInterface.initialise()
        Peripherals.motion_sensor = MotionSensor(14)
        Peripherals.laser = Laser(4)
        Peripherals.laser.turnOff()
        Peripherals.gimbal = Gimbal(3, 2)
        # used audio pins (PCM): 19 (LRC); 18 (BCLK); 21 (DIN)
        # https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/raspberry-pi-wiring
        Peripherals.audio = AudioInterface()
        Peripherals.button = Button(15)

    @staticmethod
    def destroy():
        Peripherals.laser.turnOff()
        Peripherals.gimbal.destroy()
        GpioInterface.destroy()
