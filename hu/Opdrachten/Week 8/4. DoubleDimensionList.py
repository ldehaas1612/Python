studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijfers in studentencijfers:
        gemiddeld = 0
        for cijfer in cijfers:
            gemiddeld = gemiddeld + cijfer
        antw.append("%.2f" % (gemiddeld/3))
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = 0
    total = 0
    for cijfers in studentencijfers:
        for cijfer in cijfers:
            antw = antw + cijfer
            total = total + 1
    return antw / total

print(gemiddelde_per_student(studentencijfers))

print("%.2f" % gemiddelde_van_alle_studenten(studentencijfers))