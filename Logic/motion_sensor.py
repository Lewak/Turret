from gpio_interface import GpioInterface
from gpio_interface import GpioDirections


class MotionSensor:
    def __init__(self, pin: int):
        self.pin = pin
        GpioInterface.setup(self.pin, GpioDirections.IN)

    def isMotionDetected(self) -> bool:
        return GpioInterface.readPin(self.pin)
