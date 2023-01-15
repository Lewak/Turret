from pygame import mixer
from enum import Enum
import random
from typing import Dict, List

class SfxType(Enum):
    SEARCHING = 0
    TARGETLOST = 1
    SLEEPING = 2


class AudioInterface:

    sampleNamesBySfxTypes = {
        SfxType.SEARCHING:  ['searching_1', 'searching_2', 'searching_3', 'searching_4', 'searching_5'],
        SfxType.TARGETLOST: ['searching_again_1', 'searching_again_2', 'searching_again_3'],
        SfxType.SLEEPING: ['resting_1', 'resting_2', 'resting_3', 'resting_4', 'resting_5', 'resting_6']
    }

    effectList: Dict[SfxType, List[mixer.Sound]] = {}

    def __init__(self):
        mixer.init()
        for sfxType, sampleNames in self.sampleNamesBySfxTypes.items():
            self.effectList[sfxType] = [mixer.Sound('audio/' +value + '.wav') for value in sampleNames]

    def playRandomEffect(self, effect: SfxType):
        mixer.Channel(0).play(random.choice(self.effectList[effect]))
