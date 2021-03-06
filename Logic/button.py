from gpio_interface import GpioInterface


class Button:
    def __init__(self, pin: int):
        self.pin = pin
        GpioInterface.setup(self.pin, GpioInterface.IN)

    def isPressed(self) -> bool:
        return not GpioInterface.readPin(self.pin)
