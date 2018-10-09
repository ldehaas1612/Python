tuple = {'a','b','c','d','b'}
dictionary = dict({0:'a',1:'b',2:'c',3:'d',1:'b'})
setType = set(tuple)
list = ['a','b','c','d','b']


# Jup, online gevonden.. Maar dat mag de pret niet drukken, Het is wel goeie code
def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or \
           cls.__gt__ != object.__gt__


def is_iterable(my_object):
    try:
        _ = (e for e in my_object)
    except TypeError:
        return False
    return True


print(is_sortable(tuple))
print(is_sortable(dictionary))
print(is_sortable(setType))
print(is_sortable(list))

print(is_iterable(tuple))
print(is_iterable(dictionary))
print(is_iterable(setType))
print(is_iterable(list))

print(tuple)
print(dictionary)
print(setType)
print(list)