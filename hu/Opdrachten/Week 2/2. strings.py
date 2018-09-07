word = 'Supercalifragilisticexpialidocious'

print("The word is", len(word), "characters long")
if(word.count('ice') > 0):
    print('The word contains ice')
else:
    print("The word doesn't contains ice")

w1 = 'Antidisestablishmentarianism'
w2 = 'Honorificabilitudinitatibus'

if(len(w1) > len(w2)):
    print('The word', w1, 'is bigger')
else:
    print('The word', w2, 'is bigger')

componists = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
componists.sort()
print(componists)