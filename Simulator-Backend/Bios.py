class Bios:
    clock = None
    visualization = None
    ram = None
    def __init__(self):
        pass

    def getClock(self):
        return self.clock

    def getVisualization(self):
        return self.visualization

    def getRam(self):
        return self.ram

    def setValues(self, yml):
        for i in range(len(yml)):
            if(yml[i][0]!="#"):
                if("clock" in yml[i]):
                    clockline = yml[i].split()
                    self.clock = float(clockline[1])

                if("visualization" in yml[i]):
                    pass
                print(yml[i])

    