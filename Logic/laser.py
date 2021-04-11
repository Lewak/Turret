from gpio_interface import GpioInterface
from gpio_interface import GpioDirections


class Laser:
    def __init__(self, pin: int):
        self.pin = pin
        GpioInterface.setup(self.pin, GpioDirections.OUT)

    def turnOn(self) -> None:
        GpioInterface.writePin(self.pin, True)

    def turnOff(self) -> None:
        GpioInterface.writePin(self.pin, False)
