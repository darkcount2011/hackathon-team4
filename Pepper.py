from TextToSpeech import TextToSpeech
from Tablet import Tablet
from Posture import Posture

# Create a Pepper class
class Pepper:
    # create a constructor with optional port
    def __init__(self, ip, port=9559):
        self._ip = ip
        self._port = port
        self.tts = TextToSpeech(self)
        self.posture = Posture(self)
        self.tablet = Tablet(self)