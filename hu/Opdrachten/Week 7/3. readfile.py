f= open("Kaartnummers.txt","r")
lines = f.readlines()

highest = 0
linenumber = 0
i = 0
for line in lines:
    i = i + 1
    user = line.strip('\n').split(', ')
    number = int(user[0])
    if(number > highest):
        highest = number
        linenumber = i

print("deze file kent",i,"regels")
print("Het grootste kaartnummer is", highest,"en deze staat op regel", linenumber)
f.close()