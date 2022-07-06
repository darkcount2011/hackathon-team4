from EnvironmentVariables import EnvironmentVariables
from Pepper import Pepper

env_variables = EnvironmentVariables.load()

pepper = Pepper(env_variables["PEPPER_IP"])

# pepper.sleep()
# pepper.wake()
# pepper.leds.off()1

# pepper.leds.fade_chest(20, 100, 50, 0.5)
# pepper.leds.fade_face(20, 100, 50, 0.5)
# pepper.tts.say("Good afternoon! My name is Pepper.")
# # pepper.leds.fade_chest(20, 100, 50, 0.5)
# # pepper.leds.fade_face(20, 100, 50, 0.5)
# # pepper.posture.crouch()
# # pepper.posture.stand()
# pepper.leds.fade_chest(20, 50, 100, 0.5)
# pepper.leds.fade_face(20, 50, 100, 0.5)

# pepper.navigation.explore(4.0)

# # pepper.navigation.visualize_map()

# # pepper.leds.chroma_mode()
# # pepper.motion.disableAll()
# # pepper.motion.enableAll()
# # pepper.navigation.explore(16.0)