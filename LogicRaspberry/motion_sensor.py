from gpio_interface import GpioInterface


class MotionSensor:
    def __init__(self, pin: int):
        self.pin = pin
        GpioInterface.setup(self.pin, GpioInterface.IN)

    def isMotionDetected(self) -> bool:
        return GpioInterface.readPin(self.pin)
