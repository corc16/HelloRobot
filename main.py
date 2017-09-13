from gopigo import *


class Piggy(object):
    def __init__(self):
        print("Hello, I'm your robot")
        self.dance()

    def dance(self):
        fwd()
        time.sleep(1.5)
        right_rot()
        time.sleep(.5)
        stop()


Owen = Piggy()
