from EnvironmentVariables import EnvironmentVariables
from Pepper import Pepper

env_variables = EnvironmentVariables.load()

pepper = Pepper(env_variables["PEPPER_IP"])

# for i in range(0, 10):
    # pepper.posture.crouch()
    # pepper.posture.stand()

pepper.tablet.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.gannett-cdn.com%2F-mm-%2F05e97d16e7fb53439a4222e53dcba47d4d31dde8%2Fc%3D0-97-1280-584%2Flocal%2F-%2Fmedia%2FUSATODAY%2FUSATODAY%2F2014%2F06%2F04%2F1401911998000-AP-Color-Cosmos.jpg")

# for i in range(0, 5):
    # pepper.posture.crouch()
    # pepper.posture.stand()
# pepper.tts.say("Hello I am standing!")
# pepper.tts.say("Hi there Mr 8.8!")