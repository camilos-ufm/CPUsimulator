
from IC import *
from RAM import RAM
from ALU import ALU
from Register import Register
from ORegister import ORegister
from Clock import Clock

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
        #clock
        self.clock = Clock(manufacturer,build_date,"This component manages the time", clock)
        #Registers
        self.a = Register(manufacturer,build_date,"Register A", 4, "")
        self.b = Register(manufacturer,build_date,"Register B", 4, "")
        self.c = Register(manufacturer,build_date,"Register C", 4, "")
        self.d = Register(manufacturer,build_date,"Register D", 4, "")
        self.pc = Register(manufacturer,build_date,"Program Counter", 4, 0)
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
        pos = int(RAMLoc)
        data = self.ram.getData(pos)
        print(f"Succesfully loaded 'RAM[{pos}]={data}' into Register: A")
        self.a.setData(data)

    def LD_B(self, RAMLoc):
        pos = int(RAMLoc)
        data = self.ram.getData(pos)
        print(f"Succesfully loaded 'RAM[{pos}]={data}' into Register: B")
        self.b.setData(data)

    def AND(self, arg):
        reg1 = arg[0]
        reg2 = arg[1]
        value1 = reg1.getData()
        value2 = reg2.getData()
        comparison = self.alu.AND(reg1, reg2)      # calls the alu logic operation 'or'
        print(f"Register {reg1}: {value1}\nRegister {reg2}: {value2}\And: {comparison}")
        return comparison

    def ILD_A (self, constant):
        constant = int(constant)
        self.a.setData(constant)
        print(f"Succesfuly loaded {self.a.getData()} into Register A")

    def STR_A (self, addr):
        data = self.a.getData()
        addr = int(addr)
        data = int(data)
        self.ram.setData(addr, data)
        print(f"Succesfuly wrote {self.a.getData()} into RAM address: {addr}")

    def STR_B (self, addr):
        data = self.b.getData()
        addr = int(addr)
        data = int(data)
        self.ram.setData(addr, data)
        print(f"Succesfuly wrote {self.b.getData()} into RAM address: {addr}")

    def OR(self, arg):  
        reg1 = self.twoBitToRegLetter.get(arg[0]) # extracts the first 2-bit from the 8bit value
        reg2 = self.twoBitToRegLetter.get(arg[1]) # extracts the first 2-bit from the 8bit value
        value1 = reg1.getData()
        value2 = reg2.getData()
        comparison = self.alu.OR(reg1, reg2)      # calls the alu logic operation 'or'
        print(f"Register {reg1}: {value1}\nRegister {reg2}: {value2}\Or: {comparison}")
        return comparison

    def ILD_B(self, constant):
        constant = int(constant)
        self.b.setData(constant)
        print(f"Succesfuly read {self.b.getData()} into Register B")

    def ADD(self, arg):
        reg1 = self.twoBitToRegLetter.get(arg[0]) # extracts the first 2-bit from the 8bit value
        reg2 = self.twoBitToRegLetter.get(arg[1]) # extracts the first 2-bit from the 8bit value
        value1 = reg1.getData()
        value2 = reg2.getData()
        addition = self.alu.ADD(value1,value2)
        self.reg2.setData(addition)
        print(f"Register {reg1}: {value1}\nRegister {reg2}: {value2}\Addition: {addition}")

    def SUB(self, arg):
        reg1 = self.twoBitToRegLetter.get(arg[0]) # extracts the first 2-bit from the 8bit value
        reg2 = self.twoBitToRegLetter.get(arg[1]) # extracts the first 2-bit from the 8bit value
        value1 = reg1.getData()
        value2 = reg2.getData()
        substraction = self.alu.SUB(value1,value2)
        self.reg2.setData(substraction)
        print(f"Register {reg1}: {value1}\nRegister {reg2}: {value2}\Substraction: {substraction}")

        

    def JMP(self, arg):
        self.pc = arg

    def JMP_N(self, arg):
        if (self.alu.getNegative() is not 1):
            self.JMP(arg)
        else:
            pass
        
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
        "1011": JMP,
        "JMP": JMP,
        "1100": JMP_N,
        "JMP_N": JMP_N
    }

    # Dictionary that returns for each 2bit code a letter corresponding to a reg
    twoBitToRegLetter = {
        "00": a,
         "A": a,
        "01": b,
         "B": b,
        "10": c,
         "C": c,
        "11": d,
         "D": d
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
                self.clock.next()


    def fetch(self, codeline):
        self.decode(codeline)

    def decode(self, lineOfCode):
        stringFunction = lineOfCode.split()[0]
        print(f"strFunction: {stringFunction}")
        function = self.intructionSetTable.get(stringFunction)
        print(f"function: {function}")
        self.pc.data += 1
        self.ir = function
        if (len(lineOfCode.split()) == 3):
            arguments = lineOfCode.split()[1:]
            arguments = list(map(int, arguments))
            print(arguments)
        else:
            arguments = lineOfCode.split()[1]
        self.execute(function, arguments)

    def execute(self, function, param):
        function(self, param)

    def printStatus(self):
        return "status:"     