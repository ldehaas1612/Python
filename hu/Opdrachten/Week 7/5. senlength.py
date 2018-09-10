sentence = input("Voer een zin in: ")

def gemiddelde(sentence):
    i = 0
    total = 0
    for word in sentence.split(' '):
        total = total + len(word)
        i=i+1
    return total/i

print(gemiddelde(sentence))