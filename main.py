import RPi.GPIO as GPIO
import time

horizontalServoPIN = 3
verticalServoPIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(horizontalServoPIN, GPIO.OUT)
GPIO.setup(verticalServoPIN, GPIO.OUT)

horizontalServo = GPIO.PWM(horizontalServoPIN, 50)
verticalServo = GPIO.PWM(verticalServoPIN, 50)

horizontalServo.start(12.5)
verticalServo.start(12.5)
time.sleep(2)
#try:
   # while True:
   # horizontalServo.ChangeDutyCycle(12.5)
   # horizontalServo.ChangeDutyCycle(12.5)
   #  time.sleep(0.5)
   #  verticalServo.ChangeDutyCycle(5.5)
   #  verticalServo.ChangeDutyCycle(5.5)
   #  time.sleep(0.5)
horizontalServo.ChangeDutyCycle(8.5)
verticalServo.ChangeDutyCycle(8.5)
time.sleep(2)

#except KeyboardInterrupt:
horizontalServo.stop()
verticalServo.stop()
GPIO.cleanup()