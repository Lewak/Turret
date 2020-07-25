import pigpio


class Servo:
    minPosition = 500
    maxPosition = 2500

    def __init__(self, pin):
        self.pin = pin
        self.pinInterface = pigpio.pi()

    def setAngle(self, angleDegrees):
        position = angleDegrees*(Servo.maxPosition - Servo.minPosition)/180 + Servo.minPosition
        position = min(position, Servo.maxPosition)
        position = max(position, Servo.minPosition)
        self.pinInterface.set_servo_pulsewidth(self.pin, position)

    def destroy(self):
        self.pinInterface.stop()

