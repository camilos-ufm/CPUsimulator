from IC import *

class CU(IC):
    def function1(self):
        return ""

def OUTPUT(arg):
    return print(arg)

def LD_A(arg):
    return print(arg)

intructionSetTable = {
    "0000": OUTPUT,
    "0001": LD_A,
    "year": 1964
}

def getFunction(opcode):
    return intructionSetTable[opcode]

getFunction("0000")("hola")

code = open(".code", "r")
codelines = code.readlines()

for line in codelines:
    if(line[0]!="#"):
        intructionSetTable[line[0:4]](line[4:])

#print(code.read())

 
