from IC import *

class Clock(IC):
    def __init__(self, manufacturer, build_date, purpose, speed):
        super().__init__(manufacturer, build_date, purpose)
        self.speed = speed