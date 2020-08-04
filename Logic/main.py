import time
from laser import Laser
from gimbal import Gimbal
import atexit
from random_path_generator import randomPathGenerator

laser = Laser(4)
gimbal = Gimbal(3, 2)
generator = randomPathGenerator(0.0001, 90, 90)
laser.turnOn()


def shutdownSystem():
    laser.turnOff()
    gimbal.destroy()


atexit.register(shutdownSystem)

while True:
    tupla = next(generator)
    print(tupla)
   # print(next(generator))

    time.sleep(1/30)
    gimbal.setPosition(tupla[0], tupla[1])

    # laser.turnOn()
    # time.sleep(1)
    # laser.turnOff()
    # gimbal.setPosition(90, 90)
    # time.sleep(1)







