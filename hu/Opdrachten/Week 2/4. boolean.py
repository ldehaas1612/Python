a = 6
b = 7
c = (a+b)/2


voornaam = "Luc"
tussenvoegsel = "de"
achternaam = "Haas"
mijnnaam = voornaam+" "+tussenvoegsel+" "+achternaam

print("is 75 groter dan a en kleiner dan b:",75 > a and 75 < b)
print("is mijnnaam hetzelfde als de som van alle lossen namen:",len(mijnnaam) == len(voornaam)+len(tussenvoegsel)+len(achternaam))
print("is mijnnaam net zo lang als 5x het tussenvoegsel:",len(mijnnaam) == len(tussenvoegsel)*5)
print("komt het tussenvoegsel voor in de achternaam:",achternaam.count(tussenvoegsel) > 0)