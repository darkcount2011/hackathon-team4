from naoqi import ALProxy

class Leds:
    def __init__(self, pepper):
        self.leds = ALProxy("ALLeds", pepper._ip, pepper._port)
    
    def fade_ears(self, intensity=0.5, fade_duration=1):
        self.leds.fade("EarLeds", intensity, fade_duration)
    
    def fade_face(self, red=0, green=0, blue=0, fade_duration=1):
        self.leds.fadeRGB("FaceLeds", red, green, blue, fade_duration)

    def fade_chest(self, red=0, green=0, blue=0, fade_duration=1):
        self.leds.fadeRGB("ChestLeds", red, green, blue, fade_duration)