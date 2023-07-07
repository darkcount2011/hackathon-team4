from naoqi import ALProxy

class Tracker():
    def __init__(self, pepper):
        self.tracker = ALProxy("ALTracker", pepper._ip, pepper._port)
        self.motion = ALProxy("ALMotion", pepper._ip, pepper._port)
    
    def track(self):
        self.motion.wakeUp()

        print("Time to show the cup!")

        targetName = "WhiteCup"
        cupSize = 0.2
        self.tracker.registerTarget(targetName, cupSize)

        mode = "Head"
        self.tracker.setMode(mode)

        self.tracker.setEffector("LArm")

        self.tracker.track(targetName)

        import time
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Interrupted by user")
            print("Stopping...")

        # Stop tracker.
        self.tracker.stopTracker()
        self.tracker.unregisterAllTargets()
        self.tracker.setEffector("None")

        self.motion.rest()