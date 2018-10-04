groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', "Helmond 't hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}

print("De overeenkomende stations zijn: ",set(groen).intersection(set(bruin)))
print("De stations die de bruine route anders heeft dan de groene route: ",set(bruin).difference(set(groen)))
print("Alle stations op beide routes zijn: ",set(bruin).intersection(set(groen)).union(set(bruin).symmetric_difference(set(groen))))