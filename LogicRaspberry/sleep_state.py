from peripherals import Peripherals
from audio_interface import SfxType
from state_machine import State
from serial_interface import Serial

class SleepState(State):
    def routine(self) -> State:
        from searching_state import SearchingState
        if Peripherals.motion_sensor.isMotionDetected(): # TODO Add time delay after losing sight of target
            return SearchingState()
        else:
            return self

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.SLEEPING)
        Peripherals.laser.turnOff()
