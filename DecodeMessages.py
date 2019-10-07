def shiftLeft(charAtoZ,shiftValue):
    secondRow=charAtoZ[1]
    secondRow=secondRow[shiftValue:]+secondRow[:shiftValue]
    charAtoZ[1]=secondRow


def decodeMessage(charAtoZ,codedMessage):
    codedMessage = list(codedMessage)
    firstRow = charAtoZ[0]
    secondRow = charAtoZ[1]
    decodedWord = ""
    for i in codedMessage:
        if (i == "*"):
            decodedWord += " "
        else:
            pos = secondRow.index(i)
            decodedWord += firstRow[pos]
    return decodedWord


def main():
    charAtoZ = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]
    shiftValue = int(input("Please enter the shift value: "))
    shiftLeft(charAtoZ,shiftValue)
    # print(charAtoZ)
    codedMessage = input("Please enter the coded message: ")
    while(codedMessage != "ZZZ" and codedMessage != "zzz"):
        print("The coded message is: ", codedMessage)
        decodedMessage=decodeMessage(charAtoZ,codedMessage)
        print("The decoded message is: ", decodedMessage)

        codedMessage = input("Please enter the coded message: ")

if __name__ == "__main__":
    main()
