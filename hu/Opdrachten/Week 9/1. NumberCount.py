number = 1
som = 0
i = 0
while number != 0:
    number = int(input("Geef een getal: "))
    som = som + number
    i = i + 1
print("Er zijn", i-1, "getallen ingevoerd. De som daarvan is:",som)