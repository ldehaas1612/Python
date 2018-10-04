invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
numbers = invoer.split('-')
uitvoer = []

for number in numbers:
    num = int(number)
    uitvoer.append(num)

lowest = min(uitvoer)
highest = max(uitvoer)
total = sum(uitvoer)
uitvoerlen = len(uitvoer)

uitvoer.sort()
print("Gesorteerde list van ints:",uitvoer)
print("Grootste getal:",highest,"en Kleinste getal:",lowest)
print("Aantal getallen:",uitvoerlen,"en Som van de getallen:",total)
print("Gemiddelde van deze getallen is:",(total/uitvoerlen))