maand = int(input("kies een nummer van een maand (1 t/m 12) :"))
if(maand >= 3 and maand <= 5):
    seizoen = 'Lente'
elif(maand >= 6 and maand <= 8):
    seizoen = 'Zomer'
elif(maand >= 9 and maand <= 11):
    seizoen = 'Herfst'
elif(maand == 12 or maand > 0 and maand <= 2):
    seizoen = 'Winter'
else:
    seizoen = 'Ongeldige maand'
print(seizoen)