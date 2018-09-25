clientInput = 0
aantalKluizen = 12
# kluisList = [1,2,3,4,5,6,7,8,9,10,11,12]

def toon_aantal_kluizen_vrij():
    f = open("kluisjes.txt", "r")
    lines = f.readlines()
    f.close()
    return "Er zijn nog "+str(aantalKluizen-len(lines))+" kluisjes beschikbaar"

def nieuwe_kluis():
    kluisList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    f = open("kluisjes.txt", "r")
    lines = f.readlines()
    for line in lines:
        fullLine = line.split(";")
        if int(fullLine[0]) in kluisList: kluisList.remove(int(fullLine[0]))
    f.close()
    if len(kluisList) > 0:
        wachtwoord = ""
        while len(wachtwoord) < 4:
            wachtwoord = input("Geef een wachtwoord op voor de kluis. (minimaal 4 characters lang) ")
        locker = kluisList[0]
        f = open("kluisjes.txt", "a+")
        f.writelines(str(locker)+";"+wachtwoord+"\n")
        f.close()
        response = "Uw kluisnummer is: "+str(locker)+"\nTot ziens"
    else:
        response = "Geen kluisjes meer beschikbaar.."
    return response

def kluis_openen():
    response = ""
    f = open("kluisjes.txt", "r")
    lines = f.readlines()
    if len(lines) > 0:
        kluis = int(input("Welke kluis wilt u openen? "))
        ww = input("Typ uw wachtwoord om de kluis te ontgrendelen: ")
        for line in lines:
            fullLine = line.split(";")
            if int(fullLine[0]) == kluis and fullLine[1][:-1] == ww:
                response = "Het kluisje is nu eenmalig geopend."
            else:
                if response != "Het kluisje is nu eenmalig geopend.":
                    response = "De combinatie van kluis en wachtwoord komt niet overeen."
    else:
        response = "Er zijn nog geen kluisjes bezet"
    f.close()
    return response

def kluis_teruggeven():
    f = open("kluisjes.txt", "r")
    lines = f.readlines()
    f.close()
    newLines = ""
    if len(lines) > 0:
        kluis = int(input("Welke kluis wilt u teruggeven? "))
        ww = input("Typ uw wachtwoord om de kluis vrij te geven: ")
        for line in lines:
            fullLine = line.split(";")
            if int(fullLine[0]) == kluis and fullLine[1][:-1] == ww:
                response = "Het kluisje is nu vrijgegeven."
            else:
                newLines = newLines + line
        f = open("kluisjes.txt", "w")
        f.write(newLines)
        f.close()
    else:
        response = "Er zijn nog geen kluisjes bezet"
    return response

while clientInput != 5:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Ik wil stoppen")
    clientInput = int(input("Maak uw Keuze (1, 2, 3, 4, 5):"))
    if clientInput == 1:
        print(toon_aantal_kluizen_vrij())

    elif clientInput == 2:
        print(nieuwe_kluis())

    elif clientInput == 3:
        print(kluis_openen())

    elif clientInput == 4:
        print(kluis_teruggeven())

    elif clientInput == 5:
        print("Oke, Tot ziens!")
    else:
        print("Dit is niet een valide input.")
        clientInput=0