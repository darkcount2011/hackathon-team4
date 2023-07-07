from naoqi import ALProxy

class TextToSpeech:
    DEFAULT_PITCH = 1.0
    DEFAULT_SPEED = 3.0
    DEFAULT_VOLUME = 80.0
    DEFAULT_LANGUAGE = "English"

    def __init__(self, pepper):
        self.tts = ALProxy("ALTextToSpeech", pepper._ip, pepper._port)
        self.reset()

    def say(self, message):
        self.tts.say(message)
    
    def volume(self, volume):
        self.tts.setParameter("volume", volume)
    
    def pitch(self, pitch):
        self.tts.setParameter("pitchShift", pitch)
    
    def speed(self, speed):
        self.tts.setParameter("speed", speed)

    def reset(self):
        self.tts.setParameter("pitchShift", self.DEFAULT_PITCH)
        self.tts.setParameter("speed", self.DEFAULT_SPEED)
        self.tts.setParameter("volume", self.DEFAULT_VOLUME)
        self.tts.setLanguage(self.DEFAULT_LANGUAGE)