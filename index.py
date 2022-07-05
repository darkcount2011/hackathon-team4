from EnvironmentVariables import EnvironmentVariables
from Pepper import Pepper

env_variables = EnvironmentVariables.load()

pepper = Pepper(env_variables["PEPPER_IP"])
# pepper.tts.volume(100)
# pepper.tts.pitch(0.75)
# pepper.tts.say("Good evening!")

pepper.leds.chroma_mode()

# pepper.leds.fade_ears(0, 1)
# pepper.leds.fade_face(0, 200, 255, 1)
# pepper.leds.fade_chest(255, 0, 255, 1)
# pepper.stop()

# pepper.posture.crouch()
# pepper.posture.stand()

# pepper.navigation.explore(20.0)
# pepper.navigation.visualize_map()