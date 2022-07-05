from naoqi import ALProxy

# read file contents
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# load variables from file
def load_variables(file_name):
    variables = {}
    for line in read_file(file_name).splitlines():
        if line.startswith('#'):
            continue
        if '=' not in line:
            continue
        k, v = line.split('=', 1)
        variables[k] = v
    return variables

VARIABLES = load_variables(".env")
print(VARIABLES)

tts = ALProxy(
    "ALTextToSpeech",
    VARIABLES["PEPPER_IP"],
    VARIABLES["PEPPER_PORT"]
)

tts.say("Hello, world!")

# Robotic operating System - Tip van Daan
