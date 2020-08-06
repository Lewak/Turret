from gpio_interface import GpioInterface


class Laser:
    def __init__(self, pin: int):
        self.pin = pin
        GpioInterface.setup(self.pin, GpioInterface.OUT)

    def turnOn(self):
        GpioInterface.writePin(self.pin, True)

    def turnOff(self):
        GpioInterface.writePin(self.pin, False)
