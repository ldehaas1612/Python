invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
numbers = invoer.split('-')
uitvoer = []

total=0
highest = 0
lowest = 999
sum=0

for number in numbers:
    num = int(number)
    sum=sum+num
    total=total+num
    if(num>highest):
        highest=num
    elif(num<lowest):
        lowest=num
    uitvoer.append(num)
uitvoer.sort()
uitvoerlen = len(uitvoer)
print("Gesorteerde list van ints:",uitvoer)
print("Grootste getal:",highest,"en Kleinste getal:",lowest)
print("Aantal getallen:",uitvoerlen,"en Som van de getallen:",total)
print("Gemiddelde van deze getallen is:",(total/uitvoerlen))