
import time
from laser import Laser
from gimbal import Gimbal
import atexit

laser = Laser(4)
gimbal = Gimbal(3, 2)

def pack_the_shit():
    laser.turnOff()
    print("dupa")
    gimbal.destroy()


atexit.register(pack_the_shit)

while True:
    gimbal.setPosition(50, 50)
    laser.turnOn()
    time.sleep(1)
    laser.turnOff()
    gimbal.setPosition(90, 90)
    time.sleep(1)






