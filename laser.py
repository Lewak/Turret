import RPi.GPIO as GPIO

class Laser:
    def __init__(self, pin):
        self.pin = pin

    def turnOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turnOff(self):
        GPIO.output(self.pin, GPIO.LOW)

