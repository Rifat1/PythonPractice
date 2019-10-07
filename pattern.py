

def largeToSmall(n):
    if n == 1:
        return n*"*"
    else:
        print(n*"*")
        return largeToSmall(n-1)


def smallToLarge(n):
    # if n==0:
    #     return 0
    if n == 1:
        print(n*"*")
    else:
        return(smallToLarge(n-1), print(n*"*"))


def main():
    intVal = int(input("Please enter an integer value to start the pattern: "))
    print(largeToSmall(intVal))

    print(smallToLarge(intVal))


if __name__ == "__main__":
    main()
