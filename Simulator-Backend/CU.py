from IC import *
from RAM import RAM
from ALU import ALU
from Register import Register
from ORegister import ORegister

class CU(IC):
    #attributes for CU
    ram = [None] * 16
    alu = None
    #registers
    a = None
    b = None
    c = None
    d = None
    #special register for output
    oR = None
    clock = None
    visualizations = None

    def __init__(self, manufacturer, build_date, purpose, ram, clock, visualizations):
        super().__init__(manufacturer, build_date, purpose)
        self.ram = RAM(manufacturer, build_date, "Random access memory", 16, ram) #RAM
        self.alu =  ALU(manufacturer, build_date, "Arithmetic and Logic unit") #ALU
        #Registers
        self.a = Register(manufacturer,build_date,"Register A", 4, "")
        self.b = Register(manufacturer,build_date,"Register B", 4, "")
        self.c = Register(manufacturer,build_date,"Register C", 4, "")
        self.d = Register(manufacturer,build_date,"Register D", 4, "")

        self.oR = ORegister(manufacturer,build_date,"Output Register", 4, "")
        self.visualizations = visualizations

    # Intruction Set Table 
    def OUTPUT(self, arg):
        pos = int(arg,2) #convert binary to decimal
        data = self.ram.getData(pos) #retrieve data from RAM at position pos
        self.oR.setData(data) #set data into ORegister

        return "message loaded into ORegister"

    def LD_A(self, arg):
        return arg

    # Dictionary with commands and functions
    intructionSetTable = {
    "0000": OUTPUT,
    "OUTPUT": OUTPUT,
    "0001": LD_A
    }

    def getFunction(self, opcode, arg):
        return self.intructionSetTable[opcode](self, arg)
         

# ---------------------------------------------------------------------
def main():
    ram = [1] * 16
    cu = CU("intel", "2019-08-16", "manage everything", ram, 1.2, True)

    code = open(".code", "r")
    codelines = code.readlines()

    for line in codelines:
        if(line[0]!="#"):
            print(cu.getFunction((line[0:4]),line[4:]))

if __name__== "__main__":
  main()





 
