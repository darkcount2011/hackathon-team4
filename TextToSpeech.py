from naoqi import ALProxy

class TextToSpeech:
    DEFAULT_PITCH = 1.0
    DEFAULT_SPEED = 1.0
    DEFAULT_VOLUME = 100.0
    DEFAULT_LANGUAGE = "English"

    def __init__(self, ip, port):
        self.tts = ALProxy("ALTextToSpeech", ip, port)

    def say(self, message):
        # change the pitch of the voice
        self.tts.setParameter("pitchShift", self.DEFAULT_PITCH)
        # change the speed of the voice
        self.tts.setParameter("speed", self.DEFAULT_SPEED)
        # change the volume of the voice
        self.tts.setParameter("volume", self.DEFAULT_VOLUME)
        # change the language of the voice
        self.tts.setLanguage(self.DEFAULT_LANGUAGE)

        self.tts.say(message)
        print(message)
    
    def volume(self, volume):
        self.tts.setParameter("volume", volume)