lijst = ['a', 'b', 'c']
print(lijst)

def wijzig(array):
    array.clear()
    array.extend(['d','e','f'])

wijzig(lijst)
print(lijst)