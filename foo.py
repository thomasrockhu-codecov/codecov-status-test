import sys
import time


def bar():
    if sys.version_info >= (3, 9):
        time.sleep(90)
    else:
        time.sleep(30)
