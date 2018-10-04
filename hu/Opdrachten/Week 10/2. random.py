from random import randint

def monopolyWorp():
    steen1 = 0
    steen2 = 0
    dubbels = 0
    while steen1 == steen2:
        steen1 = randint(1, 6)
        steen2 = randint(1, 6)
        if(dubbels <2):
            print(steen1,"+",steen2,'=',steen1+steen2,("(dubbel)" if steen1 == steen2 else ""))
        else:
            print(steen1,"+",steen2,'=',steen1+steen2,"GA DIRECT NAAR DE GEVANGENIS!")
            break;
        dubbels += 1

monopolyWorp()