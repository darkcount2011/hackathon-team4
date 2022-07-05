from naoqi import ALProxy 
import numpy as np
from PIL import Image

class Navigation:
    def __init__(self, pepper):
        self.navigation = ALProxy("ALNavigation", pepper._ip, pepper._port)
        self.motion = ALProxy("ALMotion", pepper._ip, pepper._port)

    def explore(self, radius=2.0):
        self.motion.wakeUp()

        error_code = self.navigation.explore(radius)
        if error_code != 0:
            print("Exploration failed! Error code: " + error_code)
            return
        
        path = self.navigation.saveExploration()
        print("Exploration saved at path: \"" + path + "\"")
        self.navigation.startLocalization()
        self.navigation.navigateToInMap([0.0, 0.0, 0.0])
        self.navigation.stopLocalization()

        self.visualize_map()
    
    def visualize_map(self):
        # self.navigation.loadExploration("/home/nao/.local/share/Explorer/2022-07-05T234428.544Z.explo")

        result_map = self.navigation.getMetricalMap()
        map_width = result_map[1]
        map_height = result_map[2]

        img = np.array(result_map[4]).reshape(map_width, map_height)
        img = (100 - img) * 2.55 # from 0..100 to 255..0
        img = np.array(img, np.uint8)
        Image.frombuffer("L",  (map_width, map_height), img, "raw", "L", 0, 1).show()