from peripherals import Peripherals
from audio_interface import SfxType
from random_path_generator import randomPathGenerator
from state_machine import State


class SearchingState(State):

    def __init__(self):
        self.generator = randomPathGenerator(0.0001, 90, 90)
        self.timer = 0

    def routine(self) -> State:
        from sleep_state import SleepState
        nextPosition = next(self.generator)
        Peripherals.gimbal.setPosition(nextPosition[0], nextPosition[1])
        self.timer += 1
        if self.timer >= 5*30:
            return SleepState()
        else:
            return self

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.SEARCHING)
        Peripherals.laser.turnOn()
