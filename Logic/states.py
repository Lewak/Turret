
#from searching_state import SearchingState
from peripherals import Peripherals
from audio_interface import SfxType
from random_path_generator import randomPathGenerator
from state_handlers import State


class SleepState(State):
    def __init__(self):
        State.__init__(self)

    def routine(self) -> State:
        if Peripherals.motion_sensor.isMotionDetected():
            return SearchingState()
        else:
            return None

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.TARGETLOST)
        Peripherals.laser.turnOff()



class SearchingState(State):
    def __init__(self):
        State.__init__(self)
        self.generator = randomPathGenerator(0.0001, 90, 90)
        self.timer = 0

    def routine(self) -> State:
        nextPosition = next(self.generator)
        Peripherals.gimbal.setPosition(nextPosition[0], nextPosition[1])
        self.timer += 1
        if self.timer >= 5*30:
            return SleepState()
        else:
            return None

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.SEARCHING)
        Peripherals.laser.turnOn()
