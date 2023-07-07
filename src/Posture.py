from naoqi import ALProxy

class Posture:
    def __init__(self, pepper):
        self.posture = ALProxy("ALRobotPosture", pepper._ip, pepper._port)

    def crouch(self):
        self.setPosture("Crouch")

    def sit(self):
        self.setPosture("Sit")

    def relax(self):
        self.setPosture("SitRelax")

    def stand(self):
        self.setPosture("Stand")
    
    def setPosture(self, name, duration=1.0):
        self.posture.goToPosture(name, duration)