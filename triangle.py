import math
def printArea():
    a = float(input("Enter the length of side 1: "))
    b = float(input("Enter the length of side 2: "))
    c = float(input("Enter the length of side 3: "))
    s = (a+b+c)/2.0
    if (isValidTriangle(a,b,c)):
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("The area of the triangle is", format(area, '.2f'))
    else:
        print("Not a valid triangle!")


def isValidTriangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

def main():
    numTriangle = int(input("How many triangles are to be processed? "))
    for i in range(numTriangle):
        printArea()

main()
