from pygame import mixer
from enum import Enum
import random


class SfxTypes(Enum):
    SEARCHING = 0
    TARGETLOST = 1


class AudioInterface:

    sampleNamesBySfxTypes = {
        SfxTypes.SEARCHING:  ['searching_1', 'searching_2', 'searching_3', 'searching_4', 'searching_5'],
        SfxTypes.TARGETLOST: ['searching_again_1', 'searching_again_2', 'searching_again_3']
    }
    effectList = {}

    def __init__(self):
        mixer.init()
        for sfxType, sampleNames in self.sampleNamesBySfxTypes.items():
            self.effectList[sfxType] = [mixer.Sound(value + '.wav') for value in sampleNames]

    def playRandomEffect(self, effect: SfxTypes):
        random.choice(self.effectList[effect]).play()
