from naoqi import ALProxy

class Motion:
    def __init__(self, pepper):
        self.mover = ALProxy("ALMotion", pepper._ip, pepper._port)
    
    def setFallProtection(self, enabled):
        self.mover.setFallManagerEnabled(enabled)
    
    def setCollisionProtection(self, enabled):
        self.mover.setFallManagerEnabled(enabled)
    
    def setSmartStiffness(self, enabled):
        self.mover.setSmartStiffnessEnabled(enabled)
    
    def setDiagnosisEffector(self, enabled):
        self.mover.setDiagnosisEffectEnabled(enabled)
    
    def setExternalCollisionProtection(self, enabled):
        self.mover.setExternalCollisionProtectionEnabled(enabled)
    
    def setPushRecovery(self, enabled):
        self.mover.setPushRecoveryEnabled(enabled)

    def enableAll(self):
        self.mover.setFallManagerEnabled(True)
        self.mover.setSmartStiffness(True)
        self.mover.setDiagnosisEffectEnabled(True)
        self.mover.setExternalCollisionProtectionEnabled(True)
        self.mover.setPushRecoveryEnabled(True)

    def disableAll(self):
        self.mover.setFallManagerEnabled(False)
        self.mover.setSmartStiffness(False)
        self.mover.setDiagnosisEffectEnabled(False)
        self.mover.setExternalCollisionProtectionEnabled(False)
        self.mover.setPushRecoveryEnabled(False)