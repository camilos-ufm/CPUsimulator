from Register import Register


class PC(Register):
    instructions = [None] * 16

    def __init__(self, manufacturer, build_date, purpose, storage, data):
        super().__init__(manufacturer, build_date, purpose, storage)
        self.instructions.append(data)
    
    def setData(self, data):
        self.instructions.append(data)
    
    def getData(self):
        return self.instructions