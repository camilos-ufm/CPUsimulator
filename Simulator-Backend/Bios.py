class Bios:
    clock = None
    visualization = []
    ram = []
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
                    for j in range(1,5):
                        self.visualization.append(yml[i+j].split(": ")[1].strip("\n"))

                if("RAM:" in yml[i]):
                    if not "t" in yml[i]:
                        for j in range(1,17):
                            self.ram.append(int(yml[i+j].split("- ")[1]))
                print(yml[i])

    