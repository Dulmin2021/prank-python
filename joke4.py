#This script will cause the computer to beep at random intervals.

import time
import random
import os

def annoying_beeps():
    while True:
        time.sleep(random.uniform(5, 15))  # Wait for a random time between 5 and 15 seconds
        os.system('echo -e "\a"')  # Send a beep sound

annoying_beeps()
