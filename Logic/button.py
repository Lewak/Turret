from gpio_interface import GpioInterface
from gpio_interface import GpioDirections


class Button:

    def __init__(self, pin: int):
        self.pin = pin
        GpioInterface.setup(self.pin, GpioDirections.IN)

    def isPressed(self) -> bool:
        return not GpioInterface.readPin(self.pin)
