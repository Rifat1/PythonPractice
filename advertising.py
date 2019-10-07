class Advert:
    __totalNumOfJobs=0
    TAX=1.15
    def __init__(self, adSize="S", duration="Q"):
        self.__adSize = adSize
        self.__duration = duration
        Advert.__totalNumOfJobs += 1
        self.__adID = str(self.__totalNumOfJobs)+self.__adSize+self.__duration
    def getTotalNumJobs(self):
        return self.__totalNumOfJobs
    def getAdSize(self):
        return self.__adSize
        

    def getDuration(self):
        if (self.__duration=="Q"):
            return "3 Months"
        elif (self.__duration=="H"):
            return "6 Months"
        elif (self.__duration=="Y"):
            return "12 Months"

    def getAdID(self):
        return self.__adID
    def setDuration(self,duration):
        self.__duration=duration
    def getAdCost(self):
        if (self.__adSize == "S" and self.__duration == "Y"):
            cost = (5000+500+4300)*self.TAX
            return cost
        elif (self.__adSize == "S" and self.__duration == "H"):
            cost = (5000+500+3100)*self.TAX
            return cost

        elif (self.__adSize == "S" and self.__duration == "Q"):
            cost = (5000+500+2300)*self.TAX
            return cost
        elif (self.__adSize == "M" and self.__duration == "Y"):
            cost = (5000+1200+4300)*self.TAX
            return cost
        elif (self.__adSize == "M" and self.__duration == "H"):
            cost = (5000+1200+3100)*self.TAX
            return cost

        elif (self.__adSize == "M" and self.__duration == "Q"):
            cost = (5000+1200+2300)*self.TAX
            return cost

        elif (self.__adSize == "L" and self.__duration == "Y"):
            cost = (5000+3200+4300)*self.TAX
            return cost
        elif (self.__adSize == "L" and self.__duration == "H"):
            cost = (5000+3200+3100)*self.TAX
            return cost

        elif (self.__adSize == "L" and self.__duration == "Q"):
            cost = (5000+3200+2300)*self.TAX
            return cost
    def __str__(self):
        return " {}\n Ad ID: {}\n Ad Size: {}\n Duration: {}\n Total Cost is {}\n".format(self.myName(),self.getAdID(),self.getAdSize(),self.getDuration(), self.getAdCost())
    @classmethod
    def myName(cls):
        return cls.__name__


class NewspaperAd(Advert):
    def __init__(self, adSize="S", duration="Q",adColour=False):
        super().__init__(adSize,duration)
        self.__adColour=adColour

    def getAdColour(self):
        return self.__adColour
    def getAdCost(self):
        if(self.__adColour):
            return super().getAdCost()
        else:
            return super().getAdCost()


    def __str__(self):
        return " Newspaper Advert\n Ad ID: {}\n Ad Size: {}\n Duration: {}\n Colour? {}\n Total Cost is {}\n".format(self.getAdID(), self.getAdSize(), self.getDuration(), self.getAdColour(), round(self.getAdCost(), 2))


class OnlineNewspaperAd(NewspaperAd):
    def __init__(self, adSize="S", duration="Q", premium=False):
        super().__init__(adSize, duration)
        self.__premium=premium
        self.__adColour=True
    def getPremium(self):
        return self.__premium
    def getAdCost(self):
        if (self.__premium):
            return super().getAdCost()-(500*self.TAX)
        else:
            return super().getAdCost()-(1000*self.TAX)

    def __str__(self):
        return " Online Newspaper Advert\n Ad ID: {}\n Ad Size: {}\n Duration: {}\n Colour? {}\n Premium Location? {}\n Total Cost is {}\n".format(self.getAdID(), self.getAdSize(), self.getDuration(), self.getAdColour(), self.getPremium(), round(self.getAdCost(), 2))

def main():

    ad=Advert("L","Y")
    print(ad)
    ad = Advert("S", "H")
    print(ad)


    newsAd=NewspaperAd("M","H",True)
    print(newsAd)
    newsAd = NewspaperAd("L", "Q", False)
    print(newsAd)

    onlineNews=OnlineNewspaperAd("S","Q",True)
    print(onlineNews)
    onlineNews = OnlineNewspaperAd("L", "Y", False)
    print(onlineNews)
    print("The total number of jobs completed are: ", onlineNews.getTotalNumJobs())

if __name__ == "__main__":
    main()
