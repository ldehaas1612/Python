def countNames(names):
    for name,times in names.items():
        if times == 1:
            print("er is", times, "student die", name, "heet")
        else:
            print("er zijn",times,"studenten die",name,"heten")

def namen():
    naam = " "
    names = {}
    while naam != "":
        naam = input("Geef een naam op: ")
        if naam in names.keys():
            old = names[naam]
            names[naam] = old+1
        else:
            if naam != '':
                names[naam] = 1
    countNames(names)

namen()