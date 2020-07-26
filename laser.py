import RPi.GPIO as GPIO

class Laser:
    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def turnOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turnOff(self):
        GPIO.output(self.pin, GPIO.LOW)
