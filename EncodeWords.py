def encodeTheWord(w):
    encodedWord = ""
    lenWord = len(w)
    if (lenWord % 2 == 0):
        lenWord = lenWord//2
    else:
        lenWord = lenWord//2+1
    for i in range(lenWord):
        first = w[0]
        last = w[-1]
        w = w[1:len(w)-1]
        encodedWord += first+last
    return encodedWord


def main():
    word = input("Please enter a word (zzz to finish): ")
    while(word != "zzz"):
        if (len(word) < 4):
            print("The word can not be processed as it is not at least 4 characters long")

        else:
            print("The original given word is: " + word)
            print("The encoded word is: "+encodeTheWord(word))
        word = input("Please enter a word (zzz to finish): ")


if __name__ == "__main__":
    main()
