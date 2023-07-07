from naoqi import ALProxy

class Tablet:
    def __init__(self, pepper):
        self.pepper = pepper
        self.memory = ALProxy("ALMemory", pepper._ip, pepper._port)
        self.tablet = ALProxy("ALTabletService", self.pepper._ip, self.pepper._port)
    
    def image(self, url):
        self.tablet.showImage(url)