import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from random_path_generator import randomPathGenerator
import random
import math

plt.style.use('ggplot')
plt.ion()
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
plotValues, = ax.plot([], [], '-o', alpha=0.8)
plt.axis([0, 180, 0, 180])
initAngle = random.uniform(0, 360)
initialXPosition = 90 + math.sin(initAngle) * 40
initialYPosition = 90 + math.cos(initAngle) * 40
pathGenerator = randomPathGenerator(90, 90, initialXPosition, initialYPosition)
xValues = []
yValues = []

while True:
    newPoint = next(pathGenerator)
    xValues = (xValues + [newPoint[0]])[-100:]
    yValues = (yValues + [newPoint[1]])[-100:]
    plotValues.set_data(xValues, yValues)
    plt.pause(1/300000)
