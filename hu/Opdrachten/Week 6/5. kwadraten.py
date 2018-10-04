numbers = [5,3,8,-15,16,-21,7,2,22]

def kwadraten_som(grondgetallen):
    total = 0
    for grondgetal in grondgetallen:
        if grondgetal > 0:
            total = total + grondgetal**2
    return total

print(kwadraten_som(numbers))