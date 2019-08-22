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

    def OR(self, num1, num2):
        return int((num1 != 0) or (num2 != 0)) # returns 1 if any of nums is not == 0, else 0

    def AND(self, num1, num2):
        return int((num1 !=0) and (num2 !=0))

    def ADD(self, num1, num2):
        return num1 + num2

    def SUB(self, num1, num2):
        substraction = abs(num1 - num2)
        if substraction < 0:
            self.negative = 1
        elif substraction == 0:
            self.zero = 1
        else:
            pass
        return substraction