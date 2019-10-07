
import random
def initializeList(lst):
    for i in range(50):
        lst.append(random.randint(1, 50))

def freqCount(frequency,randNumbers):
    
    oneToTen = 0
    elevenToTwenty = 0
    twentyoneToThirty = 0
    thirtyoneToFourty = 0
    FourtyoneToFifty = 0
    for i in range(len(randNumbers)):
        if randNumbers[i] >= 1 and randNumbers[i] <= 10:
            oneToTen += 1
        elif randNumbers[i] >= 11 and randNumbers[i] <= 20:
            elevenToTwenty += 1
        elif randNumbers[i] >= 21 and randNumbers[i] <= 30:
            twentyoneToThirty += 1
        elif randNumbers[i] >= 31 and randNumbers[i] <= 40:
            thirtyoneToFourty += 1
        else:
            FourtyoneToFifty += 1
    frequency[0] = oneToTen
    frequency[1] = elevenToTwenty
    frequency[2] = twentyoneToThirty
    frequency[3] = thirtyoneToFourty
    frequency[4] = FourtyoneToFifty

def printHistogram(frequency):
    print("A histogram of the frequency counts: \n")
    print(" 1-10:", frequency[0]*"*")
    print("11-20:", frequency[1]*"*")
    print("21-30:", frequency[2]*"*")
    print("31-40:", frequency[3]*"*")
    print("41-50:", frequency[4]*"*")



def main():
    frequency=[0]*5
    randNumbers=[]
    initializeList(randNumbers)
    print("List of random numbers:")
    print(randNumbers,"\n")
    freqCount(frequency, randNumbers)
    print("List of frequency counts:")
    print(frequency,"\n")
    printHistogram(frequency)
    


if __name__ == "__main__":
    main()
