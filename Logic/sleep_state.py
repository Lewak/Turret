from peripherals import Peripherals
from audio_interface import SfxType
from state_machine import State


class SleepState(State):

    def routine(self) -> State:
        from searching_state import SearchingState
        if Peripherals.motion_sensor.isMotionDetected():
            return SearchingState()
        else:
            return self

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.TARGETLOST)
        Peripherals.laser.turnOff()

