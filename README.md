# hackathon-team4
Hacking by the sea 2023 - Team 4

# Update
1. Create the `.env` file by duplicating the `.env.example` file and setting the correct IP.
2. Make sure you have Docker installed.
3. Run `docker compose up`

# Legacy instructions below:

# Installing python
For this project a specific version of python is required.
This version is Python 2.7.10 32-bit.
This can be downloaded from here: https://www.python.org/downloads/release/python-2710/
You will need the X86 installer for windows.

# Installing naoqi
Download the Python 2.7 SDK (zip file) from the following website:
https://www.softbankrobotics.com/emea/en/support/pepper-naoqi-2-9/downloads-softwares/former-versions?category=108
Extract the zip file and open the folder.
Copy the three folders inside the folder to a new folder of your choice.
Create a new environmental variable called "PYTHONPATH" and set the value to the path of the newly created folder.
Now you should be able to import naoqi in python.

Official docs:
https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/sdks/python-sdk/python-sdk-installation-guide

# Interesting reads
https://github.com/cltl/pepper and https://github.com/leolani/pepper
