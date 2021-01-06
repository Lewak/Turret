from peripherals import Peripherals
from audio_interface import SfxType
from random_path_generator import randomPathGenerator
from random_path_generator import StateProgress
from state_machine import State
import random
import math


class SearchingState(State):

    def __init__(self):
        initAngle = random.uniform(0, 360)
        initialXPosition = 90 + math.sin(initAngle) * 40
        initialYPosition = 90 + math.cos(initAngle) * 40
        self.generator = randomPathGenerator(90, 90, initialXPosition, initialYPosition)
        self.timer = 0

    def routine(self) -> State:
        from sleep_state import SleepState
        positionX, positionY, stateProgress = next(self.generator)
        Peripherals.gimbal.setPosition(positionX, positionY)


    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.SEARCHING)
        Peripherals.laser.turnOn()
