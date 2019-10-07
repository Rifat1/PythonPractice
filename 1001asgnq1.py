municipalities=int(input("Please enter the number of municipalities: "))
highestPop,lowestPop,totalPop=0,0,0
for i in range(municipalities):
    municipality=input("Enter the municipality: ")
    population=float(input("Enter the population: "))
    # print(i)
    # lowestPop=population
    if population>highestPop:
        highestPop=population
        highMun=municipality
    if (population<lowestPop or i==0):
        lowestPop=population
        lowMun=municipality
    totalPop+=population
average = totalPop/municipalities
print("the municipality with the highest population of "+str(highestPop)+ " million was "+highMun)
print("the municipality with the lowest population of " +
      str(lowestPop) + " million was ")
print("the range of population amounts for the "+str(municipalities)+" municipalities is "+str(highestPop-lowestPop)+" million")
print("the average population amounts for the "+str(municipalities) +
      " municipalities is "+"%.2f" % round(average, 2)+" million")


