x = 1
listaNumeros = list()
while(x > 0) :
    entrada = input('ingrese cada numero seguido de Enter, para finalizar precione Enter\n')    

    try:
        numero = int(entrada)

    except:
        print('caracter no valido, vuelva a intentarlo')
        break
    
    listaNumeros.append(numero)

listaNumeros.sort()


print('los numeros ingresados ordenados de menor a mayor son: ',listaNumeros)
