import math
import random


def randomPathGenerator(dt: float, xCenter: float, yCenter: float ):

    initAngle = random.uniform(0, 360)
    xPosition = xCenter + math.sin(initAngle)*40
    yPosition = yCenter + math.cos(initAngle)*40

    xAcceleration = 0
    yAcceleration = 0

    xVelocity = (yCenter - yPosition)*11
    yVelocity = (xPosition - xCenter)*11

    harmonicRatioX = 83
    harmonicRatioY = 217

    while True:
        for i in range(100):
            xPosition += xVelocity * dt
            yPosition += yVelocity * dt

            xVelocity += xAcceleration * dt #+ random.uniform(0, 0)
            yVelocity += yAcceleration * dt #+ random.uniform(0, 0)

            xAcceleration = (xCenter - xPosition) * harmonicRatioX + random.uniform(-0.01, 0.01)
            yAcceleration = (yCenter - yPosition) * harmonicRatioY + random.uniform(-0.01, 0.01)

        yield xPosition, yPosition
