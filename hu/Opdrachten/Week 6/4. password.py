def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def new_password(old, new):
    isAtleast6Characters = len(new) >= 6
    isDifferent = old != new

    return isDifferent and isAtleast6Characters and hasNumbers(new)

print(new_password(input("Wat is het oude wachtwoord: "),input("Wat is het nieuwe wachtwoord: ")))