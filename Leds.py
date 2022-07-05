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
    
    def chroma_mode(self):
        i = 0
        while i < 36000:
            r, g, b = self.hsl2rgb(i % 360, 1, 1)
            self.fade_chest(r, g, b, 0.2)
            self.fade_face(r, g, b, 0.2)
            i += 60
        
    def hsl2rgb(self, hue, saturation, value):
        if saturation == 0:
            return value, value, value
        else:
            hue = hue / 60
            i = int(hue)
            f = hue - i
            p = value * (1 - saturation)
            q = value * (1 - saturation * f)
            t = value * (1 - saturation * (1 - f))
            if i == 0:
                return value, t, p
            elif i == 1:
                return q, value, p
            elif i == 2:
                return p, value, t
            elif i == 3:
                return p, q, value
            elif i == 4:
                return t, p, value
            elif i == 5:
                return value, p, q