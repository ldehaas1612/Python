def new_password(old,new):
    if old != new:
        if len(new) >= 6:
            if hasNumbers(new):
                return True
    return False

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

oldPass = input("Wat is het oude wachtwoord: ")
newPass = input("Wat is het nieuwe wachtwoord: ")
print(new_password(oldPass,newPass))