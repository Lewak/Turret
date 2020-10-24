from pygame import mixer
from enum import Enum
import random


class SfxType(Enum):
    SEARCHING = 0
    TARGETLOST = 1


class AudioInterface:

    sampleNamesBySfxTypes = {
        SfxType.SEARCHING:  ['searching_1', 'searching_2', 'searching_3', 'searching_4', 'searching_5'],
        SfxType.TARGETLOST: ['searching_again_1', 'searching_again_2', 'searching_again_3']
    }
    effectList = {}

    def __init__(self):
        mixer.init()
        for sfxType, sampleNames in self.sampleNamesBySfxTypes.items():
            self.effectList[sfxType] = [mixer.Sound('audio/' +value + '.wav') for value in sampleNames]

    def playRandomEffect(self, effect: SfxType):
        random.choice(self.effectList[effect]).play()
