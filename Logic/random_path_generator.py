import math
import random
from enum import Enum


def randomPathGenerator(xCenter: float, yCenter: float, initialXPosition: float, initialYPosition: float):

    xPosition = initialXPosition
    yPosition = initialYPosition

    xAcceleration = 0
    yAcceleration = 0

    xVelocity = (yCenter - yPosition)*11  
    yVelocity = (xPosition - xCenter)*11

    harmonicRatioX = 83
    harmonicRatioY = 217
    dt = 0.0001

    for i in range(141): #4.7 sekund, to jest do zmiany
        for _ in range(100):
            xPosition += xVelocity * dt
            yPosition += yVelocity * dt

            xVelocity += xAcceleration * dt
            yVelocity += yAcceleration * dt

            xAcceleration = (xCenter - xPosition) * harmonicRatioX + random.uniform(-10000, 10000)
            yAcceleration = (yCenter - yPosition) * harmonicRatioY + random.uniform(-10000, 10000)

        yield xPosition, yPosition, False

    yield xCenter, yCenter, True


def wobbleGenerator():
    x = 0
    while True:
        x = x+1
        yield math.sin(x * 0.6) * 50 / (((x * 0.15) ** 2) + 1)
