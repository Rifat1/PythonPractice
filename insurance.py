

clientID=int(input("Please enter the client’s ID or ’0’ to quit: "))
totalPayment=0

while(clientID!=0):
    planLevel=input("Please enter the plan level as L, R or H (Low, Regular or High): ")
    coverageType=input("Please enter the type of coverage (S for single and F for family): ")
    
    
    if (coverageType=="S" or coverageType=="s"):
        if(planLevel=="L" or planLevel=="l"):
            payment=36.25
        elif(planLevel=="R" or planLevel=="r"):
            payment=48.90
        else:
            payment=69.80
        totalPayment=totalPayment+payment
    else:
        children=input("Please enter status as C or NC for (children or no children): ")
        if (children=="NC" or children=="nc"):
            if(planLevel=="L" or planLevel=="l"):
                payment=56.50
            elif(planLevel=="R" or planLevel=="r"):
                payment=74.70
            else:
                payment=99.45
        else:
            if(planLevel=="L" or planLevel=="l"):
                payment=98.35
            elif(planLevel=="R" or planLevel=="r"):
                payment=136.75
            else:
                payment=174.75
        totalPayment=totalPayment+payment   
        
    print("\nID: ", clientID)
    print("Payment: $",payment)
    clientID=int(input("\nPlease enter the client’s ID or ’0’ to quit: "))  
    print()


print("Total payment is ${:.2f}".format(totalPayment))