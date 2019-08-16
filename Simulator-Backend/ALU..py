from IC import *

class ALU(IC):
    zero = 0
    overflow = 0
    negative = 0
    def __init__(self, zero, negative, overflow):
        self.zero = zero
        self.negative = negative
        self.overflow = overflow