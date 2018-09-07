score = int(input("Geef je score:"))
geslaagd = score >= 15
if(geslaagd):
    print("Gefeliciteerd!")
else:
    print("Sorry..")
print("Met een score van", score, "ben je", ("geslaagd." if geslaagd else "gezakt."))