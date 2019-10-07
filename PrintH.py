def findThird(h):
    if h % 3 == 0:
        return h//3
    else:
        h = (h//3)+1
        return h
        # return h//3 if (h%3==0) else (h//3)+1

def printTopAndBottom(h):
    x = " "

    for i in range(h):
        print("h"*h+x*h+"h"*h)


def printMidH(h):
    for i in range(h):
        print("h"*h*3)


def main():
    height = int(input("Please enter the height of H: "))
    heightThird = findThird(height)
    printTopAndBottom(heightThird)
    printMidH(heightThird)
    printTopAndBottom(heightThird)


# if __name__ == "__main__":
#     main()

main()

