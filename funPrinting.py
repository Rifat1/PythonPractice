firstLast=input("Enter a symbol for the first and last lines: ")
secondLast=input("Enter a symbol for the second and second last lines: ")

repeatTime=int(input("How many times should the symbol repeat?: "))
firstText=input("Enter first line of text: ")
secondText=input("Enter second line of text: ")
symbolFirstText=int((repeatTime-len(firstText))/2)
symbolSecondText=int((repeatTime-len(secondText))/2)



print(firstLast*repeatTime)
print(secondLast*repeatTime)
print(","*repeatTime)
print(symbolFirstText*"/"+firstText+symbolFirstText*"/")
print(symbolSecondText*"\\"+secondText+symbolSecondText*"\\")
print(","*repeatTime)
print(secondLast*repeatTime)
print(firstLast*repeatTime)

