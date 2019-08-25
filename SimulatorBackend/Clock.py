from IC import *
import time

class Clock(IC):
    def __init__(self, manufacturer, build_date, purpose, freq):
        super().__init__(manufacturer, build_date, purpose)
        self.freq = freq

    def next(self):
        freq = self.freq
        if freq == -1:
            return 
        elif freq == 0:
            input("Press Enter to continue...")
            return
        else:
            time.sleep(1/freq)
            print("loading...")
            return