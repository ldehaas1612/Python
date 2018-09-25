results = {"Luc":9.1,"Jaap":6.9,"Pieter":7.8,"Gerrit":7.9,"Klaas":9.1,"Jesse":9.9,"Erik":4.8,"Henk":5.9}
for key, value in results.items():
    if value >= 9:
        print(key, "Heeft een", value)