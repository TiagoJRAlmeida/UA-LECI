import math
import functools

#Exercicio 4.1
impar = lambda x : x % 2 != 0

#Exercicio 4.2
positivo = lambda x : x > 0 

#Exercicio 4.3
comparar_modulo = lambda x,y : x*x < y*y

#Exercicio 4.4
cart2pol = lambda x,y : (math.sqrt(x*x + y*y), math.atan2(y,x)) 

#Exercicio 4.5
ex5 = lambda f,g,h: lambda x, y, z: h(f(x,y), g(y, z)) 

#Exercicio 4.6
def quantificador_universal(lista, f):
    return all(f(x) for x in lista
               )
#Exercicio 4.8
def subconjunto(lista1, lista2):
    return all(x in lista2 for x in lista1)    

#Exercicio 4.9
def menor_ordem(lista, f):
    return functools.reduce(lambda x, y: x if f(x, y) else y, lista)

#Exercicio 4.10 <--- Não fazer
def menor_e_resto_ordem(lista, f):
    pass

#Exercicio 5.2 <--- Mais de 1 ou 2 linhas 
def ordenar_seleccao(lista, ordem):
    pass
