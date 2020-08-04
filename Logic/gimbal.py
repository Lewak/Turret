from servo import Servo

class Gimbal:
    def __init__(self, pinServoHorizontal: float, pinServoVertical: float):
        self.servoHorizontal = Servo(pinServoHorizontal)
        self.servoVertical = Servo(pinServoVertical)

    def setPosition(self, angleHorizontalDegrees, angleVerticalDegrees):
        self.servoHorizontal.setAngle(angleHorizontalDegrees)
        self.servoVertical.setAngle(angleVerticalDegrees)

    def destroy(self):
        self.servoHorizontal.destroy()
        self.servoVertical.destroy()

