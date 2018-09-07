age = int(input("Geef je leeftijd: "))
passp = input("Heb je een Nederlands paspoort? ")
if(age >= 18 and passp.lower() == 'ja'):
    print("Gefeliciteerd, je mag stemmen!")