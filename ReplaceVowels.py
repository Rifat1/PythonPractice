word=input("Please enter a word (zzz to exit): ")

while(word!="zzz"):
    print("The original word is: "+word)
    lstWord = list(word)
    print(lstWord)
    newString=""
    for k in range(len(word)):
        # if (word[k] == "a" or word[k] == "e" or word[k] == "i" or word[k] == "o" or word[k] == "u"):
        #     lstWord[k]="*"
        first=word[k]
        word=word[1:len(word)]
        newString+=first

    print(lstWord)
    lstWord="".join(lstWord)

    print("The word without vowels is: "+lstWord)
    word = input("Please enter a word (zzz to exit): ")

