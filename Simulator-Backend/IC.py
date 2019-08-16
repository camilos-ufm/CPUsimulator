class IC:
    def __init__(self, manufacturer, build_date, purpose):
        self.manufacturer = manufacturer
        self.build_date = build_date
        self.purpose = purpose

    def getManufacturer(self):
        return self.manufacturer

    def getBuild_Date(self):
        return self.build_date

    def getPurpose(self):
        return self.purpose