# states=["alaska","bool"]
# indexValue=states.index("penny")

# def greaterFifty(a):
#     count=0
#     for i in a:
#         if i>50:
#             count=count+1
#     return count
# print(greaterFifty([45,56,23,76,50,-60]))

# def sumOdd(lst):
#     sum=0
#     for i in lst:
#         if i%2!=0:
#             sum=sum+i
#     return sum

# print(sumOdd([5,6,3,7,4,-5]))

# fname=["joe","Jack","Mehdi","rifat"]
# names=fname*2

# print(names)

# def checkDiag(a):
#     for i in range(len(a)):
#         if a[i][i]==0:
#             return False
#     return True

# print(checkDiag([[3,1,2],[0,1,3],[0,0,1]]))

# lst = [[3, 1, 2], [0, 1, 3], [0, 0, 1]]
# print(lst[2][2])

# #taking the input first
# hours = float(input("Please enter the hours used in a month:"))
# #conditions depending on the hours
# if hours <= 5:
#    charges = 100
# elif hours <= 15:
#    charges = 100+(hours-5)*25
# elif hours > 15:
#    charges = 225+(hours-15)*15
# #prints the final charges
# print("charges: $", charges)


# for i in range(1,12,4):
#     print(i, end=" ")
#This code should generate 12 6 2 0 as output.
# count = 12
# while count>=1:
#     count = count // 2
#     c = count
#     print(c+count, end=" ")
# voteId=int(input("Enter voter id number:"))
# voteAge = int(input("Enter voter age:"))
# wardNum = int(input("Enter ward number:"))
# personName = int(input("Enter voter person name:"))

# def f1(d):
#     c = v + d + f2(d) #c=2+2+f2(2)
#     return c


# def f2(c): #f2(2)
#     v = c * 2  # v=2*2=4
#     c = c + v + 1 # c=2+4+1=7
#     d = c #d=7
#     return d


# v = 2
# c = 1
# d = 1
# v = f1(v)
# print(v, c, d)


# def isWithdrawal(num):
#     if num<0:
#         return True
#     # return (num < 0)


# sum = 0
# for i in range(10):
#     number = int(input("Enter a transaction amount: "))
#     if isWithdrawal(number):
#         sum += number
# print("The sum of withdrawal amounts is:", sum)
# def freqCount():
#     lst=[0]*5
#     randNumbers = [24, 43, 44, 18, 17, 32, 8, 1, 30, 48, 13, 32, 22, 46, 10, 50, 4, 2, 23, 33, 8, 1, 25,
#                    37, 32, 48, 33, 23, 26, 31, 5, 12, 4, 9, 17, 40, 4, 31, 18, 46, 22, 46, 8, 46, 32, 18,
#                    34, 21, 34, 31]

#     print(lst)
#     oneToTen=0
#     elevenToTwenty=0
#     twentyoneToThirty=0
#     thirtyoneToFourty=0
#     FourtyoneToFifty=0
#     for i in range(len(randNumbers)):
#         if randNumbers[i]>=1 and randNumbers[i]<=10:
#             oneToTen+=1
#         elif randNumbers[i]>=11 and randNumbers[i]<=20:
#             elevenToTwenty+=1
#         elif randNumbers[i]>=21 and randNumbers[i]<=30:
#             twentyoneToThirty+=1
#         elif randNumbers[i]>=31 and randNumbers[i]<=40:
#             thirtyoneToFourty+=1
#         else:
#             FourtyoneToFifty+=1
#     lst[0]=oneToTen
#     lst[1]=elevenToTwenty
#     lst[2]=twentyoneToThirty
#     lst[3]=thirtyoneToFourty
#     lst[4]=FourtyoneToFifty
#     print(lst)
# freqCount()

codedMessage = 'FIWX*SJ*PYGO'
codedMessage = list(codedMessage)
print(codedMessage)
charAtoZ = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], [
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D']]
firstRow = charAtoZ[0]
secondRow = charAtoZ[1]
decodedWord=""
for i in codedMessage:
        if (i=="*"):
            decodedWord+=" "
        else:
            pos=secondRow.index(i)
            decodedWord+=firstRow[pos]

print(decodedWord)
