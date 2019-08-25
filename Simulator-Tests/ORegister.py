from Register import Register

class ORegister(Register):
    data = 0

    def __init__(self, manufacturer, build_date, purpose, storage, data):
        super().__init__(manufacturer, build_date, purpose, storage, data)
        self.data = data
    
    #Override setData, everything inserted in this register, will be printed out
    def setData(self, data):
        self.data = data
        print(data)
    
    def getData(self):
        return self.data

    