from servo import Servo


class Gimbal:
    def __init__(self, pinServoHorizontal: int, pinServoVertical: int):
        self.servoHorizontal = Servo(pinServoHorizontal)
        self.servoVertical = Servo(pinServoVertical)

    def setPosition(self, angleHorizontalDegrees: float, angleVerticalDegrees: float) -> None:
        self.servoHorizontal.setAngle(angleHorizontalDegrees)
        self.servoVertical.setAngle(angleVerticalDegrees)

    def destroy(self) -> None:
        self.servoHorizontal.destroy()
        self.servoVertical.destroy()
