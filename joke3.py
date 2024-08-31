# This prank creates an illusion that the computer is typing something endlessly.

import time
import random

def endless_typing():
    message = "You won't believe this... "
    while True:
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(0.1, 0.4))
        sys.stdout.write('\r')
        time.sleep(1)

endless_typing()
