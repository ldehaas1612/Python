word = ""
while len(word) != 4:
    word = input("Voer een 4 letter woord in. ")
    if len(word) != 4:
        print(word,"heeft",len(word),"letters")
    else:
        print("Inlezen van correcte string:",word,"is geslaagd")