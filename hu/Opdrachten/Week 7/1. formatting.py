def convert(celsius):
    return celsius*1.8+32

def table():
    print("C\t\t\tF")
    celsius = -30
    for i in range(0, 8):
        print(celsius,"\t\t",convert(celsius))
        celsius = celsius+10

table()