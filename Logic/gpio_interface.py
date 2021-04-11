import pigpio
from enum import Enum
from typing import Callable


class GpioDirections(Enum):
    IN = 0
    OUT = 1


class EdgeDetection(Enum):
    RISING_EDGE = pigpio.RISING_EDGE
    FALLING_EDGE = pigpio.FALLING_EDGE
    EITHER_EDGE = pigpio.EITHER_EDGE


class GpioCallbackListener:

    def cancel(self):
        pass


class GpioInterface:

    _pi = None

    @staticmethod
    def initialise() -> None:
        GpioInterface._pi = pigpio.pi()

    @staticmethod
    def destroy() -> None:
        GpioInterface._pi.stop()

    @staticmethod
    def setup(pin: int, direction: GpioDirections) -> None:
        if direction == GpioDirections.IN:
            GpioInterface._pi.set_mode(pin, pigpio.INPUT)
            GpioInterface._pi.set_pull_up_down(pin, pigpio.PUD_UP)

        else:
            GpioInterface._pi.set_mode(pin, pigpio.OUTPUT)
            GpioInterface._pi.write(pin, 0)

    @staticmethod
    def readPin(pin: int) -> bool:
        return GpioInterface._pi.read(pin)

    @staticmethod
    def writePin(pin: int, state: bool) -> None:
        GpioInterface._pi.write(pin, 1 if state else 0)

    @staticmethod
    def setServoPosition(pin: int, position: float) -> None:
        GpioInterface._pi.set_servo_pulsewidth(pin, position)

    @staticmethod
    def setPWM(pin: int, dutyCycleFraction: float, frequencyHz: int) -> None:
        dutyCycle = int(dutyCycleFraction * 255)
        GpioInterface._pi.set_PWM_frequency(pin, frequencyHz)
        GpioInterface._pi.set_PWM_dutycycle(pin, dutyCycle)

    @staticmethod
    def setCallback(pin: int, observedEdge: EdgeDetection, callbackFunction: Callable[[int, int, int], None]) -> GpioCallbackListener:
        return GpioInterface._pi.callback(pin, observedEdge.value, callbackFunction)

    @staticmethod
    def getDutyCycle(pin:int):
        return GpioInterface._pi.get_PWM_dutycycle(pin)
