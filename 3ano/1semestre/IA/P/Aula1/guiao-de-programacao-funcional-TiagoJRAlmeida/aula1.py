#Exercicio 1.1
def comprimento(lista):
    if(lista == []):
        return 0
    return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if(lista == []):
		return 0
	return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
    if(lista == []):
        return False 
    elif(lista[0] == elem):
        return True	
    return existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
	if(l2 == []):
		return l1
	l1.append(l2[0])
	return concat(l1, l2[1:])

#Exercicio 1.5
def inverte(lista):
    if(lista == []):
        return lista
    return [lista[-1]] + inverte(lista[:-1]) 

#Exercicio 1.6
def capicua(lista):
    if(lista == [] or len(lista) == 1):
        return True
    elif(lista[0] != lista[-1]):
        return False
    return capicua(lista[1:-1])


#Exercicio 1.7 
def concat_listas(lista):
    if len(lista) == 1:
        return lista[0]
    elif(lista[1] == []):
        lista.pop(1)
        return concat_listas(lista)
    else:
        lista[0].append(lista[1][0])
        lista[1].pop(0)
        return concat_listas(lista)

#Exercicio 1.8 
def substitui(lista, original, novo):
	if not lista:
		return lista
	if(lista[0] == original):
		lista[0] = novo
	return [lista[0]] + substitui(lista[1:], original, novo)

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
    if not lista1 and not lista2:
        return []
    elif not lista1:
        return [lista2[0]] + fusao_ordenada(lista1, lista2[1:])
    elif not lista2:
        return [lista1[0]] + fusao_ordenada(lista1[1:], lista2)
    elif lista1[0] < lista2[0]:
        return [lista1[0]] + fusao_ordenada(lista1[1:], lista2)
    else:
        return [lista2[0]] + fusao_ordenada(lista1, lista2[1:])

#Exercicio 1.10 <---
def lista_subconjuntos(lista):
    if not lista:
        return lista
    return [lista[0]] + lista + lista_subconjuntos(lista[1:])


#Exercicio 2.1
def separar(lista):
    if type(lista[0]) == list:
        return lista
    
    if type(lista[len(lista) - 1]) != list:
        lista.append([lista[0][0]])
        lista.append([lista[0][1]])
    else:
        lista[len(lista) - 2].append(lista[0][0])
        lista[len(lista) - 1].append(lista[0][1])
    return tuple(separar(lista[1:]))

#Exercicio 2.2
def remove_e_conta(lista, elem):
    if type(lista[1]) != list:
        lista = [lista]
        lista.append([])
        lista.append([0])
        
    if not lista[0]:
        return lista[1], lista[2][0]
    
    if lista[0][0] == elem:
        lista[2][0] += 1
    else:
        lista[1].append(lista[0][0])
    lista[0].pop(0)
    return tuple(remove_e_conta(lista, elem))

#Exercicio 3.1
def cabeca(lista):
    if not lista:
        return None
    return lista[0]

#Exercicio 3.2
def cauda(lista):
    if not lista:
        return None
    return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
    
    try:
        if type(l1[1]) != list:
            l1 = [l1]
            l1.append([])
    except:
        if len(l1) != len(l2):
            return None
        elif len(l1) == 0 :
            return []
        else:
            return [tuple([l1[0], l2[0]])]
    
    if len(l1[0]) != len(l2):
        return None
    elif not l1[0]:
        return l1[1]
    
    l1[1].append(tuple([l1[0][0], l2[0]]))
    l1[0].pop(0)
    return juntar(l1, l2[1:])
    

#Exercicio 3.4
def menor(lista):
    try:
        if type(lista[1]) != list:
            lista = [lista]
            lista.append([lista[0][0]])
    except:
        if len(lista) == 0:
            return None
        else:
            return [lista[0]]
        
    if not lista[0]:
        return lista[1][0]
    
    if lista[0][0] < lista[1][0]:
        lista[1][0] = lista[0][0]

    lista[0].pop(0)    
    return menor(lista)

#Exercicio 3.6
def max_min(lista):
    try:
        if type(lista[1]) != list:
            lista = [lista]
            lista.append([lista[0][0]])
            lista.append([lista[0][0]])
            lista[0].pop(0)    
            return max_min(lista)
    except:
        if len(lista) == 0:
            return None
        else:
            return tuple([lista[0], lista[0]])
        
    if len(lista[0]) == 1:
        if lista[0][0] > lista[1][0]:
            lista[1][0] = lista[0][0]

        if lista[0][0] < lista[2][0]:
            lista[2][0] = lista[0][0]
        return tuple([lista[1][0], lista[2][0]])
    
    if lista[0][0] > lista[1][0]:
        lista[1][0] = lista[0][0]

    if lista[0][0] < lista[2][0]:
        lista[2][0] = lista[0][0]

    lista[0].pop(0)
    return max_min(lista)
