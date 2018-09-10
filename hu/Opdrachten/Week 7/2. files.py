f= open("Kaartnummers.txt","r")
for i in range(6):
    user = f.readline().strip('\n').split(', ')
    print(user[1],"heeft kaartnummer:",user[0])
f.close()