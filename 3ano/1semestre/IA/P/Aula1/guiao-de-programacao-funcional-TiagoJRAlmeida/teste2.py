import functools

l1 = [5,4,3,1,6,1]
l2 = []

def menor_ordem(lista, f):
    return functools.reduce(f, lista)

w = lambda x,y: x < y

print(menor_ordem(l1, w))