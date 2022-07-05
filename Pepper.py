from TextToSpeech import TextToSpeech

# Create a Pepper class
class Pepper:
    # create a constructor with optional port
    def __init__(self, ip, port=9559):
        self.tts = TextToSpeech(ip, port)