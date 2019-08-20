
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
    pc = None
    ir = None
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

        self.pc = Register(manufacturer,build_date,"Program Counter",4,0)
        self.ir = Register(manufacturer,build_date,"Instruction Register",4,"")
        self.oR = ORegister(manufacturer,build_date,"Output Register", 4, "")
        self.visualizations = visualizations

    # Intruction Set Table 
    def OUTPUT(self, arg):
        pos = int(arg,2) #convert binary to decimal
        data = self.ram.getData(pos) #retrieve data from RAM at position pos
        self.oR.setData(data) #set data into ORegister

        return "message loaded into ORegister"

    def LD_A(self, RAMLoc):
        pos = int(RAMLoc,2)
        data = self.ram.getData(pos)
        self.a.setData(data)

    def LD_B(self, RAMLoc):
        pos =int(RAMLoc,2)
        data = self.ram.getData(pos)
        self.b.setData(data)

    def AND(self, arg):
        reg1= self.getRegLetter(arg[4:5])
        reg2= self.getRegLetter(arg[6:7])
        return self.alu.AND(reg1,reg2)

    def ILD_A (self, constant):
        constant=self.a

    def STR_A (self, reg):
        data = self.a.getData()
        for i in range(0, 16):
            if self.ram.getData(i) == None:
                self.ram.setData(i, data)

    def STR_B (self, reg):
            data = self.b.getData()
            for i in range(0, 16):
                if self.ram.getData(i) == None:
                    self.ram.setData(i, data)

    def OR(self, arg):
        reg1 = self.getRegLetter(arg[4:5]) # extracts the first 2-bit from the 8bit value
        reg2 = self.getRegLetter(arg[6:7]) # extracts the second 2-bit from the 8bit value
        return self.alu.OR(reg1, reg2) # calls the alu logic operation 'or'

    def ILD_B(self, const):
        self.b = const

    def ADD(self, arg):
        reg1 = self.getRegLetter(arg[4:5]) # extracts the first 2-bit from the 8bit value
        reg2 = self.getRegLetter(arg[6:7]) # extracts the second 2-bit from the 8bit value
        reg2 = self.alu.ADD(reg1,reg2)     # sets the addition to the second reg

    def SUB(self, arg):
        reg1 = self.getRegLetter(arg[4:5]) # extracts the first 2-bit from the 8bit value
        reg2 = self.getRegLetter(arg[6:7]) # extracts the second 2-bit from the 8bit value
        reg2 = self.alu.SUB(reg1,reg2)     # sets the addition to the second reg

    # Dictionary with commands and functions
    intructionSetTable = {
        "0000": OUTPUT,
        "OUTPUT": OUTPUT,
        "0001": LD_A,
        "LD_A": LD_A,
        "0010": LD_B,
        "LD_B": LD_B,
        "0011": AND,
        "AND": AND,
        "0100": ILD_A,
        "ILD_A": ILD_A,
        "0101": STR_A,
        "STR_A": STR_A,
        "0110": STR_B,
        "STR_B": STR_B,
        "0111": OR,
        "OR": OR,
        "1000": ILD_B,
        "ILD_B": ILD_B,
        "1001": ADD,
        "ADD": ADD,
        "1011": SUB,
        "SUB": SUB,

    }

    # Dictionary that returns for each 2bit code a letter corresponding to a reg
    twoBitToRegLetter = {
        "00": a,
        "01": b,
        "10": c,
        "11": d
    }

    def getFunction(self, opcode, arg):
        return self.intructionSetTable[opcode](self, arg)

    def getRegLetter(self, twobit):
        return self.twoBitToRegLetter.get(twobit)

    def initBios(self, string):
        pass

    def startInstructions(self, codelines):
        for line in codelines:
            if(line[0]!="#"):
                self.fetch(line)

    def fetch(self, codeline):
        self.decode((codeline[0:4]),codeline[4:])

    def decode(self, opcode, param):
        function = self.intructionSetTable[opcode]
        self.execute(function, param)

    def execute(self, function, param):
        function(self, param)

    def printStatus(self):
        return "status:"        