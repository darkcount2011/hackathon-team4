from Motion import Motion
from Tablet import Tablet
from Tracker import Tracker
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
        self.tablet = Tablet(self)
        self.tracker = Tracker(self)
        self.motion = Motion(self)
        self.al = ALProxy("ALAutonomousLife", self._ip, self._port)
    
    def sleep(self):
        self.al.setState("disabled")
        self.leds.off()
    
    def wake(self):
        self.al.setState("safeguard")
        self.posture.stand()