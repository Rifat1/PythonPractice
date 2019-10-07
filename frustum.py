import math
class FrustumContainer:
    __numOfContainers=0
    def __init__(self,ht=0,r1=0,r2=0):
        self.__conID = self.__numOfContainers+100
        FrustumContainer.__numOfContainers += 1
        self.__ht=ht
        self.__r1=r1
        self.__r2=r2

    def getHeight(self):
        return self.__ht

    def getRadius1(self):
        return self.__r1

    def getRadius2(self):
        return self.__r2

    def setHeight(self,height):
        self.__ht=height

    def setRadius1(self,radius1):
        self.__r1=radius1

    def setRadius2(self,radius2):
        self.__r2=radius2
    def getContainerID(self):
        return self.__conID
    def setContainerID(self,conID):
        self.__conID=conID
    def getNumberOfContainers(self):
        return self.__numOfContainers-1

    def setNumberOfContainers(self,numContainers):
        FrustumContainer.__numOfContainers=numContainers
    def computeVolume(self):
        volume=(((math.pi*self.__ht)/3)*((self.__r1**2)+(self.__r2**2)+(self.__r1*self.__r2)))/1000
        return volume

    def __str__(self):
        return "Container ID: {}\n Height: {}\n Bottom Radius: {}\n Top Radius: {}".format(self.__conID,
                                                                        self.__ht,
                                                                        self.__r1,
                                                                        self.__r2)
    def main(self):
        lst=[]
        numContainers = int(input("Please enter the number of containers: "))
        for i in range(numContainers):
            container=FrustumContainer()
            height = float(input("Enter height of the container: "))
            bottomR1 = float(input("Enter bottom radius (r1) of the container: "))
            topR2 = float(input("Enter top radius (r2) of the container: "))
            print()
            container.setHeight(height)
            container.setRadius1(bottomR1)
            container.setRadius2(topR2)
            lst.append(container)
            
        for i in range(numContainers):
            print("Container ID: ", lst[i].getContainerID())
            print("Volume: ", "%.2f" % round(lst[i].computeVolume()))
        
        print("Total number of containers: ",container.getNumberOfContainers())
        changeHeight=int(input("Enter a number from 0 to 3 to update the height of the desired container: "))
        container=lst[changeHeight]
        newHeight = float(input("Enter the new height for the container: "))
        container.setHeight(newHeight)
        print(container)
if __name__ == '__main__':
    FrustumContainer().main()
