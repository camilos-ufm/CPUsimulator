from IC import *

class ALU(IC):
    zero = 0
    overflow = 0
    negative = 0
    aGreaterThanB = 0
    equal = 0
    def __init__(self, manufacturer, build_date, purpose):
        super().__init__(manufacturer, build_date, purpose)

    def getZero(self):
        return self.zero

    def getNegative(self):
        return self.negative
    
    def getOverflow(self):
        return self.overflow

    def AND(self, num1, num2):
        return int((num1 !=0) and (num2 !=0))
