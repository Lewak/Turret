from gpio_interface import GpioInterface, GpioDirections, EdgeDetection

class StepperMotor:
    FULL_STEPS = 200
    STEP_DIVIDER = 16

    def __init__(self, stepPin: int, directionPin: int):
        self._stepPin = stepPin
        self._directionPin = directionPin
        self._absolutePosition = 0
        self._targetPosition = 0
        self._direction = None
        self.onceBefore = 0
        GpioInterface.setup(self._stepPin, GpioDirections.OUT)
        GpioInterface.setup(self._directionPin, GpioDirections.OUT)
        GpioInterface.setCallback(self._stepPin, EdgeDetection.RISING_EDGE, self.callbackFunction)
        GpioInterface.setPWM(self._stepPin, 0.1, 0)

    def setPosition(self, angleDegrees: float) -> None:
        self._targetPosition = (angleDegrees/360) * StepperMotor.FULL_STEPS * StepperMotor.STEP_DIVIDER

        if GpioInterface.getDutyCycle(self._stepPin) != 255 and self._absolutePosition != self._targetPosition:
            GpioInterface.writePin(self._directionPin, self._absolutePosition > self._targetPosition)
            self._direction = self._absolutePosition > self._targetPosition
            GpioInterface.setPWM(self._stepPin, 0.1, 10000)
            print("pwm uruchomiony")

    def destroy(self):
        GpioInterface.setPWM(self._stepPin, 0, 0)

    def callbackFunction(self, GPIO, newLevel, tick):
        if self._direction:
            self._absolutePosition += 1
        else:
            self._absolutePosition += -1

        self._direction = self._absolutePosition < self._targetPosition
       # GpioInterface.writePin(self._directionPin, self._direction)

        if self._absolutePosition == self._targetPosition:
            GpioInterface.setPWM(self._stepPin, 0, 0)

       # dupa = tick - self.onceBefore
       # self.onceBefore = tick
        #print(self._direction, self._absolutePosition, self._targetPosition, dupa)