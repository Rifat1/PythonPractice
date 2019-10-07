# weight limit of truck
# weight=0
# total package
# 
totalWeight,numPackages,eastZone,westZone,northZone,southZone=0,0,0,0,0,0
weightLimit=int(input("Please enter the weight limit of the truck: "))
while(totalWeight<1000):
    packageWeight=float(input("Please enter the weight of the package: "))
    totalWeight+=packageWeight #totalWeight=totalWeight+we
    if (totalWeight>weightLimit):
        break
    packageId=input("Please enter the package ID number: ")
    zone=input("Please enter the zone: ")
    if(zone=="East"):
        eastZone+=1
    elif(zone=="West"):
        westZone+=1
    elif(zone=="North"):
        northZone+=1
    elif(zone=="South"):
        southZone+=1
    numPackages+=1
    print("The following package is on the truck:\n Pkg No.= "+str(packageId) +
          ","+" zone = "+zone+"," + " Pkg wgt = "+"%.1f" % round(packageWeight, 1))

print(str(eastZone)+" packages are on the truck for East zone.")
print(str(westZone)+" packages are on the truck for West zone.")
print(str(northZone)+" packages are on the truck for North zone.")
print(str(southZone)+" packages are on the truck for South zone.")



print(str(numPackages)+" packages are loaded on the truck")