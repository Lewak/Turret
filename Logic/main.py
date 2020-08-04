
import time
from laser import Laser
from gimbal import Gimbal
import atexit
from random_path_generator import randomPathGenerator

laser = Laser(4)
gimbal = Gimbal(3, 2)
generator = randomPathGenerator(0.0001, 90, 90)
laser.turnOn()
def pack_the_shit():
    laser.turnOff()
    print("dupa")
    gimbal.destroy()


atexit.register(pack_the_shit)

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







