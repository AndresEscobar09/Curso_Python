print('lista de compras\n')
lista_compras =[]
while True:

    print('(1) Agregar elemento\n')
    print('(2) Borrar elemento\n')
    print('(3) ver lista\n')
    print('(4) Salir\n')
    try:
        option = int(input("ingrese la opcion que desea ejecutar\n"))
    except:
        print('Ingrese un valor numerico\n')
        continue

    if option == 1:
        element = input('ingrese el nombre del elemento\n')
        lista_compras.append(element)
        continue
    elif option == 2:
        element = input('ingrese el nombre del elemento a eliminar\n')

        for item in lista_compras:
            if item == element:
                lista_compras.remove(item)
    elif option == 3:
        print(lista_compras)
    elif option == 4:
        break
    else:
        print('eligio pcion incorreta\n')
    

