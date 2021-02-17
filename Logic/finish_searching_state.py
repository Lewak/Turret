from peripherals import Peripherals
from audio_interface import SfxType
from random_path_generator import wobbleGenerator
from state_machine import State


class FinishSearchingState(State):

    def __init__(self):
        self.generator = wobbleGenerator()
        self.timer = 0

    def routine(self) -> State:
        from sleep_state import SleepState
        positionY = next(self.generator)
        Peripherals.gimbal.setPosition(90, 90 + positionY)
        self.timer += 1
        if self.timer == 1.5*30:
            return SleepState()
        else:
            return self

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.TARGETLOST)
        Peripherals.laser.turnOn()
