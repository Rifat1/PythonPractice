class Lawncare:
    def __init__(self, propertyAddress='', numberOfVisits=0, propertyArea=0):
        self.__propertyAddress = propertyAddress
        self.__numberOfVisits = numberOfVisits
        self.__propertyArea = propertyArea

    def getPropertyAddress(self):
        return self.__propertyAddress

    def getNumVisits(self):
        return self.__numberOfVisits

    def getPropertyArea(self):
        return self.__propertyArea

    def setPropertyAddress(self, propertyAddress):
        self.__propertyAddress = propertyAddress

    def setNumVisits(self, numberOfVisits):
        self.__numberOfVisits = numberOfVisits

    def setPropertyArea(self, propertyArea):
        self.__propertyArea = propertyArea

    def amountDue(self):
        cost = 0
        if self.__propertyArea < 4000:
            cost = self.__numberOfVisits*30*1.15
        elif self.__propertyArea >= 4000 and self.__propertyArea <= 6000:
            cost = self.__numberOfVisits*40*1.15
        elif self.__propertyArea > 6000:
            cost = self.__numberOfVisits*60*1.15
        return cost


lawncare1 = Lawncare('abc', 3, 120)
lawncare1.setPropertyAddress('dfrgjhgeruajk')
print(lawncare1.getPropertyAddress())
lawncare2 = Lawncare('ijk', 7, 140)
