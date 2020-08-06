import pigpio


class Servo:
    _minPosition = 500
    _maxPosition = 2500

    def __init__(self, pin: int):
        self.pin = pin
        self.pinInterface = pigpio.pi()

    def setAngle(self, angleDegrees: float) -> None:
        position = angleDegrees*(Servo._maxPosition - Servo._minPosition)/180 + Servo._minPosition
        position = min(position, Servo._maxPosition)
        position = max(position, Servo._minPosition)
        self.pinInterface.set_servo_pulsewidth(self.pin, position)

    def destroy(self) -> None:
        self.pinInterface.stop()
