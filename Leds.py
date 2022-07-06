from naoqi import ALProxy

class Leds:
    DEFAULT_INTENSITY = 0.5
    DEFAULT_COLOR = {
        "R": 200,
        "G": 200,
        "B": 200
    }

    def __init__(self, pepper):
        self.leds = ALProxy("ALLeds", pepper._ip, pepper._port)
        self.reset()
    
    def fade_ears(self, intensity=0.5, fade_duration=1):
        self.leds.fade("EarLeds", intensity, fade_duration)
    
    def fade_face(self, red=0, green=0, blue=0, fade_duration=1):
        self.leds.fadeRGB("FaceLeds", red, green, blue, fade_duration)

    def fade_chest(self, red=0, green=0, blue=0, fade_duration=1):
        self.leds.fadeRGB("ChestLeds", red, green, blue, fade_duration)
    
    def reset(self):
        self.fade_ears(self.DEFAULT_INTENSITY)
        self.fade_face(self.DEFAULT_COLOR["R"], self.DEFAULT_COLOR["G"], self.DEFAULT_COLOR["B"])
        self.fade_chest(self.DEFAULT_COLOR["R"], self.DEFAULT_COLOR["G"], self.DEFAULT_COLOR["B"])

    def off(self):
        self.fade_ears(0, 0)
        self.fade_face(0, 0, 0, 0)
        self.fade_chest(0, 0, 0, 0)

    def chroma_mode(self):
        self.fade_ears(0, 0)
        i = 0
        while i < 36000:
            r, g, b = self.hsl2rgb(i % 360, 1, 1)
            self.fade_chest(r, g, b, 0.3)            
            self.fade_face(r, g, b, 0.3)
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