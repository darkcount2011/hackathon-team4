from EnvironmentVariables import EnvironmentVariables
from Pepper import Pepper

env_variables = EnvironmentVariables.load()

pepper = Pepper(env_variables["PEPPER_IP"])
pepper.tts.say("Who's joe?")
pepper.tts.say("Joe momma")
