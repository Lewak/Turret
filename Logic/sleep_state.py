from state import State
from peripherals import Peripherals
from audio_interface import SfxType
from searching_state import SearchingState


class SleepState(State):

    def routine(self) -> State:
        if Peripherals.motion_sensor.isMotionDetected():
            return SearchingState(self.stateMachine)
        else:
            return self

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.TARGETLOST)
        Peripherals.laser.turnOff()
