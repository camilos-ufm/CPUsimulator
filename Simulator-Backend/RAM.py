from Memory import Memory

class RAM(Memory):
    ram = [None] * 16

    def __init__(self, manufacturer, build_date, purpose, storage, ram):
        super().__init__(manufacturer, build_date, purpose, storage)
        self.ram = ram
    
    def setData(self, pos, data):
        self.ram[pos] = data
    
    def getData(self, pos):
        return self.ram[pos]

    def getRAM(self):
        return self.ram