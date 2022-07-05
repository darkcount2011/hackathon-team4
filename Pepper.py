from naoqi import ALProxy
from Leds import Leds
from Navigation import Navigation
from TextToSpeech import TextToSpeech
from Posture import Posture

# Create a Pepper class
class Pepper:
    # create a constructor with optional port
    def __init__(self, ip, port=9559):
        self._ip = ip
        self._port = port
        self.tts = TextToSpeech(self)
        self.posture = Posture(self)
        self.leds = Leds(self)
        self.navigation = Navigation(self)
    
    def stop(self):
        tmp = ALProxy("ServiceManager", self._ip, self._port)
        tmp.stopAllServices()