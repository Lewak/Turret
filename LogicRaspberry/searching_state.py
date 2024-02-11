from peripherals import Peripherals
from serial_interface import Serial
from audio_interface import SfxType
from random_path_generator import randomPathGenerator
from random_path_generator import wobbleGenerator
from state_machine import State
from finish_searching_state import FinishSearchingState
import random
import math


class SearchingState(State):
    def __init__(self):
        initAngle = random.uniform(0, 360)
        initialXPosition = 90 + math.sin(initAngle) * 40
        initialYPosition = 90 + math.cos(initAngle) * 40
        self.wobbler = wobbleGenerator()
        self.pathGenerator = randomPathGenerator(90, 90, initialXPosition, initialYPosition)

    def routine(self) -> State:
        positionX, positionY, isFinished = next(self.pathGenerator)
        Peripherals.gimbal.setPosition(positionX, positionY + next(self.wobbler))
        Serial.sendMessage("SET " + str(positionY + next(self.wobbler)) + "\n")

        if isFinished:
            return FinishSearchingState()
        else:
            return self

    def enter(self) -> None:
        Peripherals.audio.playRandomEffect(SfxType.SEARCHING)
        Peripherals.laser.turnOn()
