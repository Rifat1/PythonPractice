import random

def createList():
    lst=[]
    for i in range(20):
        lst.append(random.randint(1, 10))
    return lst

def frequency(list,givenNum):
    # count=0
    # for i in list:
    #     if i==givenNum:
    #         count+=1
    if list == []:  # base case
        return 0
    if list[0] == givenNum:
        return 1 + frequency(list[1:], givenNum)
    else:
        return 0 + frequency(list[1:], givenNum)


def main():
    enterNum = int(input("Enter an integer (1 to 10) to count its frequency in a random list: "))
    print()
    list=createList()
    frequencyOfNum=frequency(list,enterNum)
    print("The list of random numbers is:\n",list)
    print()
    print("{} occurs {} times in the given list.".format(enterNum,frequencyOfNum),"\n")

if __name__ == "__main__":
    main()
    