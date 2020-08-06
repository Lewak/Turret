import RPi.GPIO as GPIO
from enum import Enum


class GpioInterface(Enum):
    IN = 0
    OUT = 1

    @staticmethod
    def initialise() -> None:
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BCM)  # Use physical pin numbering

    @staticmethod
    def destroy() -> None:
        GPIO.cleanup()

    @staticmethod
    def setup(pin: int, direction: 'GpioInterface') -> None:
        if direction == GpioInterface.IN:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        else:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    @staticmethod
    def readPin(pin: int) -> bool:
        return GPIO.input(pin)

    @staticmethod
    def writePin(pin: int, state: bool) -> None:
        GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)
