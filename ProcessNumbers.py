def shouldProcess(n):
    if (n >= 6 and n <= 12):
        return True
    else:
        return False


def processInput(n):
    if (shouldProcess(n)):
        sum = findSum(n)
        print("The sum from 1 to "+str(n)+" is: "+str(sum))
        findDivisors(sum)
    else:
        print("Please enter an integer between 6 and 12, \n The number " +
              str(n)+" is outside of acceptable value")


def findSum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


def findDivisors(n):
    print("The divisors of "+str(n)+" are:")
    for i in range(2, n):
        if (n % i == 0):
            print(i, end=" ")


def main():
    intVal = int(input("Please enter an integer between 6 and 12: "))
    processInput(intVal)


if __name__ == "__main__":
    main()
