def code(invoerstring):
    asciiStr = ""
    for char in invoerstring:
        asciiStr += chr(ord(char)+3)
    return asciiStr

print(code(input("Geef de voornaam, beginpunt en eindpunt zonder spaties")))