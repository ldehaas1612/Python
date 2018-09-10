lijst = eval(input("Geef lijst met minimaal 10 strings: "))
lijstvan4 = []
for item in lijst:
    if len(item) == 4:
        lijstvan4.append(item)

print(lijstvan4)