
#busqueda lineal------

def linear_search(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

numeros =[64,34,25,12,22,11,90]

elemento_buscado = 11

indice = linear_search(numeros,elemento_buscado)

if indice != -1:
    print('el elemento:',elemento_buscado, 'se encuetra en el indice',indice,'\n')
else:
    print('el elemento:', elemento_buscado,'no se encuentra en la lista\n')

# ordenamiento bubble_sort

def bubble_sort(lista):
    n = len(lista)
    for i in range (n):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1] = lista [j+1], lista[j]

numeros = [64,34,25,12,22,11,90,87,30,24]
bubble_sort(numeros)
print(numeros)

#ordenamiento  insertionsort

def insertion_sort(lista):
    for i in range (1,len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = list[j]
            j -= 1
        lista[j + 1] = key
        
numeros = [64,34,25,12,22,11,90,87,30,24,78,104,233,245,876,56,49,4,531,5678,54,70,21]
insertion_sort(numeros)
print(numeros)

