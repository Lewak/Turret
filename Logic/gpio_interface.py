import pigpio


class GpioInterface:

    IN = 0
    OUT = 1
    _pi = None

    @staticmethod
    def initialise() -> None:
        GpioInterface._pi = pigpio.pi()

    @staticmethod
    def destroy() -> None:
        GpioInterface._pi.stop()

    @staticmethod
    def setup(pin: int, direction: 'GpioInterface') -> None:
        if direction == GpioInterface.IN:
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
