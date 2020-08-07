from pygame import mixer
from enum import Enum
import random


class SoundTypes(Enum):
    SEARCHING = 0
    TARGETLOST = 1

class AudioInterface:

    linker = {
        SoundTypes.SEARCHING:  ['searching_1', 'searching_2', 'searching_3', 'searching_4', 'searching_5'],
        SoundTypes.TARGETLOST: ['searching_again_1', 'searching_again_2', 'searching_again_3']
    }
    soundList = []
    effectList = []

    def __init__(self):
        mixer.init()
        for soundEffects in self.linker:
            print (soundEffects)
            for value in self.linker[soundEffects]:
                print(value)
                self.soundList.append(mixer.Sound(value + '.wav'))
            self.effectList.append(self.soundList)

    def playRandomEffect(self, effect: SoundTypes):
            print(effect.value)
            random.choice(self.effectList[effect.value]).play()
