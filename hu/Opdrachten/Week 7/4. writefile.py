import datetime

def writeToFile(name):
    if name == 'exit':
        exit()
    f=open("Hardlopers.txt", "a+")

    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")

    f.write(s+name+"\n")
    f.close()

while True:
    writeToFile(input("Geef de naam van de deelnemer"))