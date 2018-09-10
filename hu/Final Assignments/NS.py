def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM < 50:
        prijs = afstandKM * 0.8
    elif afstandKM > 0:
        prijs = 15
        prijs = prijs + (afstandKM * 0.6)
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    kosten = standaardprijs(afstandKM)
    if ((leeftijd < 12 or leeftijd >= 65) and weekendrit == False):
        kosten = kosten / 100 * 70
    elif ((leeftijd < 12 or leeftijd >= 65) and weekendrit == True):
        kosten = kosten / 100 * 65
    elif ((leeftijd >= 12 or leeftijd < 65) and weekendrit == False):
        kosten = kosten
    elif ((leeftijd >= 12 or leeftijd < 65) and weekendrit == True):
        kosten = kosten / 100 * 60
    return kosten

age = int(input("Wat is je leeftijd "))
weekend = input("Is het weekend? ")
weekend = (True if weekend == 'ja' else False)
distance = int(input("Hoeveel kilometer is de rit"))
print("Dan kost de rit:",format(ritprijs(age,weekend,distance), ".2f"), "Euro.")