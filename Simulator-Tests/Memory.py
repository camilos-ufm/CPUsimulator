from IC import *

class Memory(IC):
    def __init__(self, manufacturer, build_date, purpose, storage):
        super().__init__(manufacturer, build_date, purpose)
        self.storage = storage