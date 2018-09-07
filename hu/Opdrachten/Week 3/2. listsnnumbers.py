list = [0, 5, -14, 3, 9, 12, -3, 'aa']

list_2 = [num for num in list if isinstance(num, (int,float))]
list_2.sort()
listlength = len(list_2)
min = int(list_2[0])
max = int(list_2[listlength-1])
print("min is:",min,"and max is",max)
print("so the difference is",abs(min)+abs(max))