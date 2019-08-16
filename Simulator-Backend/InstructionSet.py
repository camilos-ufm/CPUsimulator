class InstructionSet:
    def __init__ (self):
        pass

    #@staticmethod
    def function1(self, output, ram_address):
        #output.setAddress(ram_address)
        return ""

    thisdict =	{
    "0000": function1,
    "model": "Mustang",
    "year": 1964
    }

    #print(thisdict)
    #@staticmethod
    def getFunction(self,opcode):
        return self.thisdict[opcode]
