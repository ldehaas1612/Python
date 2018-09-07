cijferICOR = 6.2
cijferPROG = 8.7
cijferCSN = 7.6
multiplier = 30

gemiddelde = str((cijferICOR+cijferPROG+cijferCSN)/3)
beloning = str(cijferICOR*multiplier+cijferPROG*multiplier+cijferCSN*multiplier)
overzicht = 'Mijn cijfers (gemiddeld een '+gemiddelde+') leveren een beloning van € '+beloning+' op!'
print(overzicht)