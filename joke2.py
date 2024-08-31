#This script displays a fake progress bar that keeps going without actually doing anything.

import time
import sys

def fake_progress_bar():
    toolbar_width = 40
    sys.stdout.write("Loading: [%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")
    print("Oops! Something went wrong! Please try again later.")

fake_progress_bar()
