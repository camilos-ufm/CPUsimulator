from Register import Register


class PC(Register):
    data = [None] * 16

    def __init__(self, manufacturer, build_date, purpose, storage, data):
        super().__init__(manufacturer, build_date, purpose, storage)
        self.data = data
    
    def setData(self, data):
        self.data.append(data)
    
    def getData(self):
        return self.data