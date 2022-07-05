from naoqi import ALProxy

class Tablet:
    def __init__(self, pepper):
        self.tablet =  ALProxy("ALTabletService", pepper._ip, pepper._port)

    def image(self, url):
        self.tablet.showImage(url)
